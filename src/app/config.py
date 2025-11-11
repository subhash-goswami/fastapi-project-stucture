import os
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from typing import List

load_dotenv()


class Settings(BaseSettings):
    """
    Application configuration using Pydantic's BaseSettings.

    Attributes:
        LOG_LEVEL (str): Logging level (e.g., "INFO", "DEBUG").
        LOGGER_NAME (str): Name to use for the application logger.
        DATABASE_URL (str): Database connection string.
        ALLOWED_ORIGINS (str): Comma-separated CORS origins.
        ENVIRONMENT (str): Application environment (development, staging, production).
        APP_NAME (str): Display name for the app.
        APP_VERSION (str): Application version.
        DEBUG (bool): Whether debug mode is enabled.
        PORT (int): Port to run the FastAPI app.
        HOST (str): Host address to bind.
    """

    # -------------------------------------------------------------------------
    # 🌐 Application Info
    # -------------------------------------------------------------------------
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Service")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    PORT: int = int(os.getenv("PORT", "8000"))
    HOST: str = os.getenv("HOST", "0.0.0.0")

    # -------------------------------------------------------------------------
    # 🧱 Database Configuration
    # -------------------------------------------------------------------------
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    # -------------------------------------------------------------------------
    # 🔐 CORS / Security Settings
    # -------------------------------------------------------------------------
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")

    # -------------------------------------------------------------------------
    # 🪵 Logging Configuration
    # -------------------------------------------------------------------------
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOGGER_NAME: str = os.getenv("LOGGER_NAME", "fastapi-app")

    # -------------------------------------------------------------------------
    # ⚙️ Utility Methods
    # -------------------------------------------------------------------------
    @property
    def get_allowed_origins(self) -> List[str]:
        """Return list of allowed origins (split by comma or wildcard)."""
        if self.ALLOWED_ORIGINS == "*":
            return ["*"]
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",") if o.strip()]

    class Config:
        env_file = ".env"


settings = Settings()
