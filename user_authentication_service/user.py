#!/usr/bin/env python3

"""
Module that defines the User model using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): primary key.
        email (str): user's email, cannot be null.
        hashed_password (str): hashed password, cannot be null.
        session_id (str, optional): session identifier.
        reset_token (str, optional): token for password reset.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: a formatted string with user details.
        """

        return (
            f"<User(email='{self.email}', "
            f"hashed_password='{self.hashed_password}', "
            f"session_id='{self.session_id}', "
            f"reset_token='{self.reset_token}')>"
        )
