import logging
from datetime import datetime

def setup_logger():
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    log_filename = f"app/data/logs/{current_time}_log.log"

    logging.basicConfig(level=logging.INFO, 
                        filename=log_filename, 
                        filemode='w',
                        format='%(asctime)s - %(name)s - %(message)s')

    return logging.getLogger(__name__)

logger = setup_logger()