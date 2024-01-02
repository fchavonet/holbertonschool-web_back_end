#!/usr/bin/env python3
""" Measuring the total execution time for wait_n(n, max_delay). """

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Parameters:
    - n (int): the number of times to execute wait_n concurrently.
    - max_delay (int): the maximum delay in seconds for each wait_n execution.

    Returns:
    - float: the average execution time per wait_n call.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
