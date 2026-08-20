import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

# File Handler
file_handler = logging.FileHandler("logfile")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# consloe handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


logger.info("The app is working..")

logger.debug("Error happens")

logger.warning("Please write a stronge password")

logger.critical("The server was crushed..")