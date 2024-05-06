#!/usr/bin/env python3
"""task module"""
import asyncio

wait_random = __import__('0-basic_async_syntax').0-basic_async_syntax


def task_wait_random(max_delay: int) -> asyncio.Task:
    """the task function"""
    result = asyncio.create_task(wait_random(max_delay))
    return result
