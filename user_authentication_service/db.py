#!/usr/bin/env python3

"""
Module for managing database interactions.
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
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

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first user that matches the given filters.

        Args:
            **kwargs: arbitrary keyword arguments to filter the query.

        Returns:
            User: the first matching user.

        Raises:
            NoResultFound: if no user matches the query.
            InvalidRequestError: if an invalid field is passed.
        """

        session = self._session

        # Validate provided column names.
        valid_columns = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in valid_columns:
                raise InvalidRequestError(f"Invalid column name: {key}")

        # Execute query with dynamic filters.
        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates the attributes of a user identified by user_id.

        Args:
            user_id (int): the ID of the user to update.
            **kwargs: keyword arguments corresponding to user attributes.

        Raises:
            ValueError: if an argument is not a valid user attribute.
            NoResultFound: if no user with the given user_id is found.
        """

        session = self._session

        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound("No user found with the given ID.")

        valid_columns = User.__table__.columns.keys()

        for key, value in kwargs.items():
            if key not in valid_columns:
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        session.commit()
