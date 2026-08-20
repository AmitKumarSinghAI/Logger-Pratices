import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

# File Handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.addHandler(console_handler)


logger.debug("Debug message")

logger.info("Application started")

logger.warning("Low memory")

logger.error("Database error")

logger.critical("Application crashed")