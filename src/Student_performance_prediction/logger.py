import logging, os
from datetime import datetime as dt
from pathlib import Path

log_filename = f"{dt.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"

log_filepath = os.path.join(Path(os.getcwd()), "logs")

os.makedirs(log_filepath, exist_ok= True)

log_file = os.path.join(log_filepath, log_filename)

logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    format="[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    logging.info("logging is ready")

