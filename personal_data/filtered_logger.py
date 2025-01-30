#!/usr/bin/env python3

"""
This module provides utilities for handling and protecting sensitive data in logs and databases.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): fields to obfuscate.
        redaction (str): string to replace field values.
        message (str): original log message.
        separator (str): character separating fields in the message.

    Returns:
        str: obfuscated log message.
    """

    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)

    return message
