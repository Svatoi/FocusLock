import time
import random

def create_app():
    from .utils import logger
    from .models import ModelMixin, Market, Task, User
    from .core import Blocker, get_processes
    from .database import setup_database, session
    from .controllers import TaskController
    
    ModelMixin.set_session(session)
    
    setup_database()
    
    bl = Blocker()
    
    ## Логика для taskcontroller 
    check_tasks_completed = False
    logger.info(f"Task is completed?: {check_tasks_completed}")
    
    user_id = session.query(User).filter(User.id == 1).first()
    tasks = TaskController.is_done_task(user_id.id)
    if tasks:
        has_active_tasks = True
        logger.info("Lockdown mode starting, some tasks is active")
    else:
        has_active_tasks = False
        
    while has_active_tasks:
        
        processes = get_processes(bl.get_blocked_processes())
        logger.info("Some blocked processes were found, start blocking")
        if processes:
            bl.block(processes)
        
        if check_tasks_completed:
            logger.info('All tasks were completed')
            break
        
        time.sleep(1)
    
    ## =======================================================
    ## Everything above is a temporary option