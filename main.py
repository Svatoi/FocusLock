from app import create_app
from app.utils import logger

if __name__ == '__main__':
    app = create_app()
    logger.info("Applications running")