#!/usr/bin/env python3

"""
Defines a Cache class that interacts with Redis.
"""

import functools
import redis
import uuid
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called using Redis INCR.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that increments the call count and calls the method.
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance.
        Connects to Redis and clears the current database.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args:
            data: the data to store.

        Returns:
            str: the key under which the data was stored.
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): the Redis key to retrieve.
            fn (Callable, optional): a function to convert the data back.

        Returns:
            The retrieved and optionally converted data, or None if not found.
        """

        value = self._redis.get(key)

        if value is None:
            return None

        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis and decode it using UTF-8.

        Args:
            key (str): the Redis key.

        Returns:
            str or None: the decoded string or None if key doesn't exist.
        """

        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis and convert it.

        Args:
            key (str): the Redis key.

        Returns:
            int or None: The converted integer or None if key doesn't exist.
        """

        return self.get(key, fn=int)
