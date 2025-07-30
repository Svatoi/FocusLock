import time

from sqlalchemy import create_engine

from .models import Base, Market, Task, User
from .utils import get_db_path, is_create_db, logger

engine = create_engine(get_db_path(), echo=True)

def setup_database() -> None:
    if not is_create_db():
        Base.metadata.create_all(engine)
        tables = list(Base.metadata.tables.keys())
        logger.info(f"New tables created: %s", tables)
    else:
        logger.debug("Tables already exist")

def create_app():
    from .core import Blocker, get_processes
    
    setup_database()
    
    bl = Blocker()
    
    process=input('Enter a list of process wich you like to ban, separated by commas: ')
    list_of_block_processes = [x.strip().lower() + '.exe' for x in process.split(',')]
    bl.add_processes(list_of_block_processes)
    
    remove_process=input('Do you want to remove one of your blocked processes?(Yes/No): ')
    if remove_process == 'No':
        pass
    if remove_process == 'Yes':
        list_process=input(f"What process do you want to remove?({list_of_block_processes}):")
        process = [x.strip().lower() + '.exe' for x in list_process.split(',')]
        bl.remove_processes(process)
        
    add_process=input('Do you want to add some processes to block list?(Yes/No): ')
    if add_process == 'No':
        pass
    if add_process == 'Yes':
        process=input(f"What process do you want to add?({list_of_block_processes}):")
        bl.add_processes(process)
    
    tasks = input('Enter some task what you want to complete: ')
    list_of_tasks = [x.lower() for x in tasks.split(',')]
    
    check_tasks_completed = False
    logger.info(f"Task is completed?: {check_tasks_completed}")
    
    has_active_tasks = bool(list_of_tasks)
    logger.info("Lockdown mode starting, some tasks is active")
    while has_active_tasks:
        
        processes = get_processes(bl.get_blocked_processes())
        logger.info("Some blocked processes were found, start blocking")
        if processes:
            bl.block(processes)
        
        if check_tasks_completed:
            logger.info('All tasks were completed')
            break
        
        time.sleep(1)