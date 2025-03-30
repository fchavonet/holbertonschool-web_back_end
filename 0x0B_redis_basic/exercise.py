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


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Store input args and output result in Redis lists.
        """

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

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
    @call_history
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


def replay(method: Callable):
    """
    Display the history of calls of a particular function.

    Args:
        method (Callable): the method whose history to display.
    """

    r = redis.Redis()
    method_name = method.__qualname__
    inputs_key = method_name + ":inputs"
    outputs_key = method_name + ":outputs"

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        input_str = inp.decode('utf-8')
        output_str = out.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output_str}")
