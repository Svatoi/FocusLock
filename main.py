import logging

from app import create_app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        filename='app/data/logs/sosak_log.log', 
                        filemode='w',
                        format='%(asctime)s - %(name)s - %(message)s')
    
    app = create_app()