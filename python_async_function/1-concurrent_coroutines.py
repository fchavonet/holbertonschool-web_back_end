#!/usr/bin/env python3
""" Async function for concurrent execution of wait_random. """

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Execute the wait_random coroutine concurrently
    `n` times with a specified `max_delay`.

    Parameters:
    - n (int): the number of times to execute wait_random concurrently.
    - max_delay (int): the maximum delay in seconds
                       for each wait_random execution.

    Returns:
    - List[float]: a list of delays in ascending order.
    """
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delay = await asyncio.gather(*tasks)

    return sorted(delay)
