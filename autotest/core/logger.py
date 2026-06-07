import logging
import os
from datetime import datetime

def get_logger():
    log_path = "logs"
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = os.path.join(log_path, f"test_{datetime.now().strftime('%Y%m%d')}.log")
    logger = logging.getLogger("auto_test")
    logger.setLevel(logging.INFO)
    # 避免重复添加handler
    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding="utf-8")
        sh = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
        fh.setFormatter(fmt)
        sh.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger