#!/usr/bin/env python3
"""
BasicAuth module for the API.
"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    Implements methods for Basic HTTP Authentication.
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): the Authorization
            header from the request.

        Returns:
            str: The Base64 part of the header or None if invalid.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Return the Base64 part (everything after "Basic ").
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 string to its original value.

        Args:
            base64_authorization_header (str): the Base64 encoded string.

        Returns:
            str: the decoded string as UTF-8, or None if invalid.
        """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string to bytes.
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert the bytes to UTF-8 string.
            return decoded_bytes.decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extract the user email and password
        from a decoded Base64 authorization header.

        Args:
            decoded_base64_authorization_header (str):
            the decoded Base64 string.

        Returns:
            tuple: A tuple (email, password) or (None, None) if invalid.
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """
        Retrieves a User instance based on email and password.

        Args:
            user_email (str): the user's email address.
            user_pwd (str): the user's password.

        Returns:
            User | None: the User instance if found and valid, otherwise None.
        """

        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Overloads Auth's current_user method to retrieve the User instance
        based on the Basic Authorization header.

        Args:
            request: the HTTP request object (optional).

        Returns:
            User | None: the authenticated user,
            or None if no user can be retrieved.
        """

        auth_header = Auth().authorization_header(request)
        b64_header = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(b64_header)
        email, password = self.extract_user_credentials(decoded)
        user = self.user_object_from_credentials(email, password)

        return user
