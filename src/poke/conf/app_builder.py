from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from src.poke.exceptions import NotFound
from src.poke.interface.endpoints import router as poke_router


async def not_found_exception_handler(
    request: Request, error_type: NotFound
) -> JSONResponse:
    return await http_exception_handler(
        request, HTTPException(HTTP_404_NOT_FOUND, detail=str(error_type))
    )


def setup_app() -> FastAPI:
    app = FastAPI()
    app.include_router(poke_router)
    app.add_exception_handler(NotFound, not_found_exception_handler)
    return app
