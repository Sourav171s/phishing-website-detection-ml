import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''Gets the current working directory (e.g., /home/user/project).

os.path.join(os.getcwd(), "logs", LOG_FILE)

Joins the path to form:
/home/user/project/logs/05_27_2025_14_30_00.log
This is a path to a log file, NOT a directory.'''
#this is path to log file not a directory
logs_path=os.path.join(os.getcwd(),"logs")
#make a log directory
os.makedirs(logs_path,exist_ok=True)
# its a final log file path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
#sample code 
'''def divide(a, b):
    logging.info("Starting divide function")
    try:
        result = a / b
        logging.info("Division successful")
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error")
        return None

print(divide(10, 2))
print(divide(10, 0))
with open("")'''