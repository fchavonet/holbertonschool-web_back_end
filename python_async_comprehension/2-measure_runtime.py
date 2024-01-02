#!/usr/bin/env python3
""" Module to measure the runtime of asynchronous comprehensions. """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing asynchronous comprehensions.

    Returns:
        float: total runtime in seconds.
    """

    start_time = time.time()

    coroutines_list = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*coroutines_list)

    end_time = time.time()

    return (end_time - start_time)
