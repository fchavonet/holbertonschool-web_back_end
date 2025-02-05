#!/usr/bin/env python3
"""
Auth module for the API.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Returns:
          - True if path is None.
          - True if excluded_paths is None or empty.
          - False if path is in excluded_paths (slash-tolerant).
        """
        if path is None or not excluded_paths:
            return True

        # Normalize the path to always have a trailing slash.
        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in the excluded paths.
        for excluded in excluded_paths:
            if excluded == normalized_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header, if present.
        For now, it returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        For now, it returns None.
        """
        return None
