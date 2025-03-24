#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json) -> None:
        """
        Test that "GithubOrgClient.org" returns the correct value.
        Test that "get_json" is called exactly once with the expected URL.
        """

        fake_payload = {"login": org, "id": 123}
        mock_get_json.return_value = fake_payload

        client_instance = GithubOrgClient(org)
        result = client_instance.org
        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, fake_payload)

    def test_public_repos_url(self) -> None:
        """
        Test that "GithubOrgClient._public_repos_url" returns the correct URL
        based on the mocked org property.
        """

        fake_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = fake_payload
            client_instance = GithubOrgClient("google")
            self.assertEqual(
                client_instance._public_repos_url,
                fake_payload["repos_url"]
            )

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """
        Test that "GithubOrgClient.public_repos" returns the list
        of repository names from the chosen payload.
        """

        get_json_mock.return_value = [
            {"name": "random_rep"},
            {"name": "random-rep1"},
        ]
        # Call the mock function to simulate its invocation.
        get_json_mock()
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mocked_public_repos:
            mocked_public_repos.return_value = [
                {"name": "rand"},
                {"name": "rand1"},
            ]
            gc = GithubOrgClient("abc")
            r = gc._public_repos_url
            self.assertEqual(r, mocked_public_repos.return_value)
            mocked_public_repos.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that "GithubOrgClient.has_license" returns the expected value
        based on the repository license information.
        """

        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for GithubOrgClient.public_repos using fixtures.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class fixtures: patch "requests.get" to return
        example payloads found in the fixtures.

        The configuration uses "side_effect" so that
        "requests.get(url).json()" returns the correct payload.
        """

        config = {
            "return_value.json.side_effect": [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }

        cls.get_patcher = patch("requests.get", **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stop the patcher.
        """

        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Test that "GithubOrgClient.public_repos" returns
        the expected list of repository names.
        """

        client_instance = GithubOrgClient("google")
        self.assertEqual(client_instance.org, self.org_payload)
        self.assertEqual(client_instance.public_repos(), self.expected_repos)
        self.assertEqual(client_instance.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self) -> None:
        """
        Test that "GithubOrgClient.public_repos" returns
        the list of repositories that have the specified license.
        """
        client_instance = GithubOrgClient("google")
        self.assertEqual(client_instance.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()


if __name__ == "__main__":
    unittest.main()
