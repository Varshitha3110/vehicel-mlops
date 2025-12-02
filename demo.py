# # below code is to check the logging config

# """
# The below code imports the file 'loggers' and perform the logging with provided statements.
# To consider that we are not calling the function here (def configure_logger()) rather trying to create the folder and files
# """
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# below code is to check the exception config
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e

# # --------------------------------------------------------------------------------

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()