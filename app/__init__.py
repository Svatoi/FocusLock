import time

from sqlalchemy import create_engine

from .models import Base, Market, Task, User
from .utils import get_db_path, is_create_db, logger

engine = create_engine(get_db_path(), echo=True)

def setup_database() -> None:
    if not is_create_db():
        Base.metadata.create_all(engine)
        logger.info(f"Tables have been created: [{Base.metadata.tables.keys()}]") 

def create_app():
    from .core import get_processes
    
    setup_database()
    
    process=input('Enter a list of process wich you like to ban, separated by commas: ')
    list_of_block_process = [x.strip().lower() + '.exe' for x in process.split(',')]
    
    tasks = input('Enter some task what you want to complete: ')
    list_of_tasks = [x.lower() for x in tasks.split(',')]
    
    check_tasks_completed = True
    
    has_active_tasks = bool(list_of_tasks)
    while has_active_tasks:
        
        processes = get_processes(block_list=list_of_block_process)
        
        if check_tasks_completed:
            break
        
        time.sleep(1)