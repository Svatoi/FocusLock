import logging

from app import create_app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    app = create_app()