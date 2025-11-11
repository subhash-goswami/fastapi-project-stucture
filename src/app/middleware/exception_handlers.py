from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from src.core.logger import logger
from src.core.common.exceptions import ApiException


async def api_exception_handler(
    request: Request, exp: ApiException | HTTPException | Exception
) -> JSONResponse:
    """
    Handles custom API exceptions and returns a structured JSON response.

    Args:
        request (Request): The incoming HTTP request.
        exp (ApiException): The raised API exception.

    Returns:
        JSONResponse: A JSON response with error details and appropriate status code.
    """
    logger.error(f"{exp.__class__.__name__} at {request.url}: {exp.message}")
    return JSONResponse(
        status_code=exp.status_code or 500,
        content={
            "error": exp.__class__.__name__,
            "details": exp.message or "Unexpected error occurred.",
            "status_code": exp.status_code or 500,
        },
    )
