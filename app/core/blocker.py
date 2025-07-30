import psutil
import time

from app.utils import logger

## Сделать так что бы ещё и блокало сайты

class Blocker():
    def __init__(self):
        self.blocked_processes = set()
        
    def add_processes(self, list_of_processes: str) -> None:
        logger.info(f"The processes: {list_of_processes} will be add to blocked processes")
        for proc in list_of_processes:
            self.blocked_processes.add(proc)
        logger.info(f"All submitted processes have been added to the blocked list")
        
    def remove_processes(self, list_of_processes: str) -> None:
        logger.info(f"The processes: {list_of_processes} will be remove from blocked processes")
        for proc in list_of_processes:
            self.blocked_processes.discard(proc)
        logger.info(f"All submitted processes have been remove \nBlocked list looks like now: {self.blocked_processes}")
        
    def get_blocked_processes(self):
        return self.blocked_processes
    
    def block(self, processes: psutil.Process) -> None:
        logger.info(f"The blocked processes found were transferred: {processes}")
        for proc in processes:
            try:
                
                logger.info("Trying to close process")
  
                
                proc.terminate()
                time.sleep(1)
                
                if not proc.is_running():
                    logger.info(f"Terminated {proc.info['name']} with PID {proc.info['pid']}")
                else:
                    logger.error(f"Error when trying terminated {proc.info['name']} with PID {proc.info['pid']}")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                logger.warning(f"Failed to terminate {proc.info['name']} with PID {proc.info['pid']}. Access Denied")
