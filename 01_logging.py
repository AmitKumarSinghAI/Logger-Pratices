import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s"
)

logging.info("Application started")