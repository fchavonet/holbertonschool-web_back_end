#!/usr/bin/env python3

"""
Unit tests for the utils module.
"""

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


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
        Tests that "access_nested_map" raises a KeyError with the expected key.
        """

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected_key)


if __name__ == "__main__":
    unittest.main()
