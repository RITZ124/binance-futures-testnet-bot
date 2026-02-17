import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_logger(name, filename):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(LOG_DIR / filename)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger