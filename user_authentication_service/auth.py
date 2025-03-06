#!/usr/bin/env python3

"""
Module providing password hashing functionality using bcrypt.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.

    Args:
        password (str): the password to hash.

    Returns:
        bytes: the salted hash of the password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)
