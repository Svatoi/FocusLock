import time


def create_app():
    from .core import get_processes, create_DB
    
    db = create_DB()
    
    process=input('Enter a list of process wich you like to ban, separated by commas: ')
    list_of_block_process = [x.strip().lower() + '.exe' for x in process.split(',')]
    
    tasks = input('Enter some task what you want to complete: ')
    list_of_tasks = [x.lower() for x in tasks.split(',')]
    
    check_tasks_completed = True
    
    has_active_tasks = bool(list_of_tasks)
    while has_active_tasks:
        
        processes = get_processes(block_list=list_of_block_process)
        
        if not check_tasks_completed:
            break
        
        time.sleep(1)