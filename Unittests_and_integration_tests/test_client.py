#!/usr/bin/env python3

"""
Unit tests for the client module.
"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


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


if __name__ == "__main__":
    unittest.main()
