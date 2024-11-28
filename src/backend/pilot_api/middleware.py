from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Callable
import humps


async def convert_to_camel_case(request: Request, call_next: Callable):
    response = await call_next(request)

    if isinstance(response, JSONResponse):
        response_data = response.json()
        camel_data = humps.camelize(response_data)
        return JSONResponse(
            content=camel_data,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
    return response
