#!/usr/bin/env python3

"""
Module for managing database interactions.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """
    A database management class to handle user-related operations.
    """

    def __init__(self) -> None:
        """
        Initializes a new database instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Returns a memoized session object for database interactions.
        If the session doesn't exist, it is created and returned.

        Returns:
            Session: an SQLAlchemy session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Create and add a new user to the database.

        Args:
            email (str): the user's email.
            hashed_password (str): the hashed password of the user.

        Returns:
            User: the created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user
