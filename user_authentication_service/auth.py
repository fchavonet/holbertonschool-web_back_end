#!/usr/bin/env python3

"""
Module providing user authentication functionality.
"""

import uuid

from db import DB
from user import User
from bcrypt import checkpw, hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt.

        Args:
            password (str): the password to hash.

        Returns:
            bytes: the hashed password.
        """

        return hashpw(password.encode("utf-8"), gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user if the email is not already taken.

        Args:
            email (str): the user's email.
            password (str): the user's password.

        Returns:
            User: the newly created user object.

        Raises:
            ValueError: if a user with the given email already exists.
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a login attempt for a given email and password.

        Args:
            email (str): the user's email.
            password (str): the user's password.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        hashed_password = user.hashed_password

        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode("utf-8")

        return checkpw(password.encode("utf-8"), hashed_password)

    def create_session(self, email: str) -> str:
        """
        Creates a new session ID for a user identified by their email.

        Args:
            email (str): the email of the user.

        Returns:
            str: the generated session ID, or None if the user does not exist.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieves a user based on the given session ID.

        Args:
            session_id (str): the session ID associated with a user.

        Returns:
            User: the corresponding user if found, otherwise None.
        """
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.

    Args:
        password (str): the password to hash.

    Returns:
        bytes: the salted hash of the password.
    """

    return hashpw(password.encode("utf-8"), gensalt())


def _generate_uuid() -> str:
    """
    Generates a new UUID string.

    Returns:
        str: a string representation of a new UUID.
    """

    return str(uuid.uuid4())
