import logging
import sys
from src.app.config import settings

LOG_LEVEL = settings.LOG_LEVEL.upper()
log_level = getattr(logging, LOG_LEVEL, logging.INFO)

# Clear existing handlers (important for reload mode)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],  # ✅ Force log to terminal
)

logger = logging.getLogger(settings.LOGGER_NAME)
