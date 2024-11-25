import os
import sys
import logging
from datetime import datetime

log_file_name=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
log_folder="logs"
log_format="[%(asctime)s] %(levelname)s %(module)s: %(message)s"
os.makedirs(os.path.join(os.getcwd(),log_folder),exist_ok=True)
log_file_path=os.path.join(os.getcwd(),log_folder,log_file_name)
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("summarizerlogger")