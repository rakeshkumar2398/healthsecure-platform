from datetime import datetime
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logging_config import logger


async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled error path=%s error=%s", request.url.path, str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "path": request.url.path,
            "timestamp": datetime.utcnow().isoformat()
        }
    )
