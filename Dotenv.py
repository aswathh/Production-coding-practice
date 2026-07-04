import os 
import logging
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

def get_env(key:str)-> Optional[str]:
    """if key is not present in .env then return None"""
    return os.getenv(key)

name:Optional[str] = get_env("APP_NAME")
log_level_str:Optional[str] = get_env("LOG_LEVEL")

if log_level_str is None:
    log_level_str = "INFO"

log_level = getattr(logging,log_level_str)

logging.basicConfig(level=log_level,format='%(asctime)s-%(filename)s-%(levelname)s-%(message)s')

logger = logging.getLogger(__name__)
logger.debug(f"App name loaded:{name}")
logger.info(f"logger initialised with the leve:{log_level_str}")
