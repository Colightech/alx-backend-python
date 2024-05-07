#!/usr/bin/env python3
"""A module that Write a coroutine called
async_generator that takes no arguments."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """this function write a coroutine called
    async_generator that takes no arguments."""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
