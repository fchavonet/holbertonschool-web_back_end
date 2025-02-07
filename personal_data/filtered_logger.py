#!/usr/bin/env python3

"""
This module provides utilities for handling
and protecting sensitive data in logs and databases.
"""

import logging
import mysql.connector
import os
import re

from mysql.connector import connection
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering PII fields.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields (List[str]): fields to be obfuscated in logs.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating sensitive data.

        Args:
            record (logging.LogRecord): log record to format.

        Returns:
            str: formatted log message with sensitive fields redacted.
        """
        # Filter sensitive fields in the message.
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
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
    # Replace values of specified fields.
    for field in fields:
        # Match "field=value" until the separator.
        pattern = f"{field}=[^{separator}]*"
        # Replace field value with redaction.
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data.

    Returns:
        logging.Logger: configured logger with a RedactingFormatter.
    """
    # Create a logger named "user_data".
    logger = logging.getLogger("user_data")
    # Set logging level to INFO.
    logger.setLevel(logging.INFO)
    # Prevent propagation of log messages to parent loggers.
    logger.propagate = False
    # Create a StreamHandler and set its formatter.
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # Add the handler to the logger.
    logger.addHandler(handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    Connect to the database using environment variables.

    Returns:
        MySQLConnection: a connection to the MySQL database.
    """
    # Read environment variables.
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database.
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    Connects to MySQL, retrieves all rows from "users",
    and logs each row with PII fields filtered.
    """
    # Connect to the database.
    db: MySQLConnection = get_db()
    cursor = db.cursor()

    # Execute query to select all rows from the "users" table.
    cursor.execute("SELECT * FROM users;")
    # Get the column names for the table.
    fields: List[str] = [desc[0] for desc in cursor.description]

    # Create and configure the logger.
    logger = get_logger()

    # Process and log each row.
    for row in cursor:
        # Map the column names to their corresponding values.
        row_dict = dict(zip(fields, row))
        # Create the log message by joining key-value pairs.
        log_message = "; ".join(
            [f"{key}={value}" for key, value in row_dict.items()])
        # Filter sensitive fields in the message.
        filtered_message = filter_datum(PII_FIELDS, "***", log_message, "; ")
        # Log the obfuscated message.
        logger.info(filtered_message)

    # Close the cursor and the database connection.
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
