from fastapi import Request
from typing import Callable


async def add_custom_header(request: Request, call_next: Callable):
    response = await call_next(request)
    return response
