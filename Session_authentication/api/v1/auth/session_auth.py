#!/usr/bin/env python3
"""
Session Authentication Module.
"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the User ID based on the given Session ID.

        Args:
            session_id (str): the session ID.

        Returns:
            str: the corresponding User ID, or None if session_id is invalid.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Get the current user from the session.

        Args:
            request (Request): the HTTP request.

        Returns:
            User: the user instance or None.
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session, effectively logging out the user.

        Args:
            request (Request): the HTTP request.

        Returns:
            bool: True if session was successfully deleted, False otherwise.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
            return True

        return False
