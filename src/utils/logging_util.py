import os

from loguru import logger


def setup_logging(log_dir: str, log_file: str = "app.log"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)
    logger.add(log_path, level="INFO", format="{time} - {level} - {message}")

    console_format = "{time} - {level} - {message}"
    logger.add(
        lambda msg: print(msg, end=""), format=console_format, level="INFO"
    )
    return logger
