#!/usr/bin/env python3

"""
Defines a Cache class that interacts with Redis.
"""

import redis
import uuid
from typing import Union


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
