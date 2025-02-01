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
