#!/usr/bin/env python3
"""
Session Authentication Module.
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session-based authentication class.
    """

    # Dictionary to store session_id -> user_id mapping.
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user_id.

        Args:
            user_id (str): the ID of the user.

        Returns:
            str: the generated session ID, or None if input is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new session ID.
        session_id = str(uuid.uuid4())

        # Store the session in the dictionary.
        self.user_id_by_session_id[session_id] = user_id

        return session_id
