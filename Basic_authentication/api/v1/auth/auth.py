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
        For now, it always returns False.
        """
        return False

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
