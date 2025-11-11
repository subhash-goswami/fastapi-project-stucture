from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.core.logger import logger
from src.app.config import settings
from src.app.middleware.exception_handlers import api_exception_handler
from src.core.common.exceptions import ApiException
from src.api.v1 import v1_router


# -----------------------------------------------------------------------------
# 🚀 Initialize FastAPI Application with Dynamic Config
# -----------------------------------------------------------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=f"{settings.APP_NAME} API — running in {settings.ENVIRONMENT} mode.",
    docs_url="/docs",
    redoc_url="/redoc",
)

# -----------------------------------------------------------------------------
# 🌐 Middleware Setup
# -----------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ⚙️ Exception Handlers
# -----------------------------------------------------------------------------
app.add_exception_handler(ApiException, api_exception_handler)

# -----------------------------------------------------------------------------
# 🔌 Register Routers
# -----------------------------------------------------------------------------
app.include_router(v1_router)

# -----------------------------------------------------------------------------
# 🏁 Startup Event
# -----------------------------------------------------------------------------
@app.on_event("startup")
async def startup_event():
    logger.info(
        f"✅ {settings.APP_NAME} (v{settings.APP_VERSION}) is running successfully "
        f"in {settings.ENVIRONMENT} mode on {settings.HOST}:{settings.PORT}"
    )

# -----------------------------------------------------------------------------
# 🔁 Root Redirect
# -----------------------------------------------------------------------------
@app.get("/", include_in_schema=False)
async def root():
    """Redirect root `/` to API docs."""
    return RedirectResponse(url="/redoc")  # or use /docs


if __name__ == "__main__":
    """
    Supports both local (CLI) and Docker runs.
    - CLI: You can still run `uvicorn src.main:app --reload`
    - Docker: It will auto-pick HOST/PORT from .env via settings
    """
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )