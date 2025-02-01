#!/usr/bin/env python3

"""
This module provides functionality for securely hashing passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and a randomly generated salt.

    Args:
        password (str): the password to hash.

    Returns:
        bytes: the hashed password.
    """
    # Encode the password to bytes (bcrypt requires bytes input).
    encoded_password = password.encode("utf-8")

    # Generate the salt and hash the password.
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate if the provided password matches the hashed password.

    Args:
        hashed_password (bytes): the hashed password to compare.
        password (str): the plain text password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Encode the plain text password to bytes.
    encoded_password = password.encode("utf-8")

    # Use bcrypt to compare the password with the hash.
    return bcrypt.checkpw(encoded_password, hashed_password)
