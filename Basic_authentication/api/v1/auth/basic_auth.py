#!/usr/bin/env python3
"""
BasicAuth module for the API.
"""

import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
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
    ) -> (str, str):
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

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
