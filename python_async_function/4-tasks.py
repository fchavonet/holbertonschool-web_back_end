#!/usr/bin/env python3
"""
Async function using asyncio Tasks
for concurrent execution of task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute the task_wait_random coroutine
    concurrently 'n' times with a specified 'max_delay'.

    Parameters:
    - n (int): the number of times to execute task_wait_random concurrently.
    - max_delay (int): the maximum delay in seconds
                       for each task_wait_random execution.

    Returns:
    - List[float]: a list of delays in ascending order.
    """
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    delay = await asyncio.gather(*tasks)

    return sorted(delay)
