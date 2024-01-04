#!/usr/bin/env python3
""" Async Generator Module. """

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Generate random numbers asynchronously.

    Yields:
        float: random number between 0 and 10.

    Raises:
        None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
