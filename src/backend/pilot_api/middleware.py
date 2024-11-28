from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import humps


class CaseConverterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if isinstance(response, JSONResponse):
            response_body = await response.json()
            camel_case_body = humps.camelize(response_body)

            return JSONResponse(
                content=camel_case_body,
                status_code=response.status_code,
                headers=dict(response.headers),
            )
        return response
