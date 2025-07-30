import os

from .comf_logger import logger
from dotenv import load_dotenv

load_dotenv()

def get_db_path() -> str:
    
    logger.info("Start getting path to db")
    db_path = os.getenv("DB_PATH")
    logger.info(f"Get path: ({db_path}) ")
    
    if not db_path:
        logger.error("ValueError: DB_PATH не вказаний в .env файл")
    
    return db_path

def is_create_db() -> bool:
    db_path = get_db_path()
    return (
        not os.path.exists(db_path)
        and os.access(os.path.dirname(db_path), os.W_OK)
    )

