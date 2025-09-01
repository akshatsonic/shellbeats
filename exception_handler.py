import sys
import logging
import traceback

def my_exception_handler(ex_type, ex_value, ex_traceback):
    # Log the unhandled exception details
    logging.error(f"{ex_type.__name__}:{ex_value}")
    logging.error(traceback.format_exception(ex_type, ex_value, ex_traceback))
    sys.exit(1)