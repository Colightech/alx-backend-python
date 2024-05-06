#!/usr/bin/env python3
"""Module that returns the list of all delays"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns list of delays in ascending order"""

    delays: List[float] = []
    all_delays: List[float] = []

    for number in range(n):
        delays.append(wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        result = await delay
        all_delays.append(result)

    return all_delays
