# import loggging

# loggging.basicConfig(level=logging.INFO)
# loggging.info("program started")
# loggging.WARNING("Invalid input")
# loggging.ERROR("Operation failed")
# print()
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Invalid input")
logging.error("Operation failed")