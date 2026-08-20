import logging

try:

    result = 10/0

except Exception:

    logging.exception("An error occurred.")
