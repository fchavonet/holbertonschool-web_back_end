#!/usr/bin/env python3
""" Module with asynchronous generators and comprehension. """

import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Asynchronously generate a list of floats.

    Returns:
        List[float]: a list of floats generated asynchronously.
    """
    return [num async for num in async_generator()]
