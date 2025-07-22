from tabulate import tabulate

def create_app():
    from .core import get_processes
    
    list_of_process=input('Enter a list of process wich you like to ban, separated by commas: ')
    list_of_block_process = '.exe'.join(list_of_process.lower().split(','))
       
    print("=== System monitoring ===")
    
    print("\nRunning prohibited processes:")
    processes = get_processes(block_list=list_of_block_process)
    print(tabulate(processes, 
                   headers=['PID', 'Name', 'CPU %', 'Память %'], 
                   tablefmt='grid'))