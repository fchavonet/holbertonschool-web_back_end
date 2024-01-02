#!/usr/bin/env python3
""" Async function for creating an asyncio Task with wait_random. """

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task to execute wait_random with a specified max_delay.

    Parameters:
    - max_delay (int): the maximum delay in seconds for wait_random.

    Returns:
    - asyncio.Task: an asyncio Task object
                    representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
