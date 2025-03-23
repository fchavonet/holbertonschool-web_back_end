#!/usr/bin/env python3

"""
Unit tests for the utils module.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing the "access_nested_map" function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict[Any, Any],
            path: Tuple[Any, ...],
            expected: Any
    ) -> None:
        """
        Test that "access_nested_map" returns the expected result.
        """

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[Any, Any],
            path: Tuple[Any, ...],
            expected_key: str
    ) -> None:
        """
        Test that "access_nested_map" raises a KeyError with the expected key.
        """

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected_key)


class TestGetJson(unittest.TestCase):
    """
    Test class for the "get_json" function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict[str, bool]
    ) -> None:
        """
        Test that "get_json" returns the expected payload.
        """

        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for the "memoize" decorator.
    """

    def test_memoize(self) -> None:
        """
        Test that memoize caches the result of a_method.
        """

        class TestClass:
            """
            Test class to validate the memoize decorator.
            """

            def a_method(self) -> int:
                """
                Returns an integer value.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                Returns the result of a_method.
                """

                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mocked_method:
            test_instance = TestClass()
            first_call = test_instance.a_property
            second_call = test_instance.a_property
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
