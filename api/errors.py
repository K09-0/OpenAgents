"""Error handling utilities for the OpenAgents API.

@fix-author: KiloClaw
@fix-date: 2026-06-07
@runtime: os=Linux, arch=x64, working_dir=/root/.openclaw/workspace/clanker_repo/api, shell=python3
"""

from typing import Optional
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Structured error response schema.

    All API errors follow this consistent format:
    - code: Machine-readable error code (e.g., VALIDATION_ERROR, NOT_FOUND)
    - message: Human-readable error message
    - details: Optional object with additional error context
    - request_id: Unique request identifier for log correlation
    """

    code: str
    message: str
    details: Optional[dict] = None
    request_id: Optional[str] = None


# Standard error codes
ERROR_NOT_FOUND = "NOT_FOUND"
ERROR_VALIDATION = "VALIDATION_ERROR"
ERROR_AUTH_FAILED = "AUTH_FAILED"
ERROR_RATE_LIMITED = "RATE_LIMITED"
ERROR_INTERNAL = "INTERNAL_ERROR"
ERROR_BAD_REQUEST = "BAD_REQUEST"


def format_error(
    code: str,
    message: str,
    details: Optional[dict] = None,
    request_id: Optional[str] = None,
) -> dict:
    """Format error response following the standard schema."""
    return {
        "code": code,
        "message": message,
        "details": details,
        "request_id": request_id,
    }