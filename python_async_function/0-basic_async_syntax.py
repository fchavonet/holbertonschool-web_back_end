#!/usr/bin/env python3
""" Asynchronous function to simulate a random delay. """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously sleeps for a random duration between 0 and max_delay.

    Parameters:
    - max_delay (int): the maximum delay in seconds (default is 10).

    Returns:
    - float: the actual random delay that occurred.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
