import psutil
from app.utils import logger

## Добавить отслеживания захода на сайты

def get_processes(block_list=[]):

    processes = []
    logger.info("Collecting information of all running processes, start")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in block_list:
                logger.info(f"It was found: {proc.info['name']} which is a prohibited")
                processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as error:
            logger.error(f"Error when try to get processes: {error}")
    return processes

