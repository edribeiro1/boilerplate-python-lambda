from logger import logger
from other import test2
import traceback

def lambda_handler():
    test2.testizinho()


lambda_handler()
# try:
#     trow_error()
# except Exception as e:
#     logger.error(e)