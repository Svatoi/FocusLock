import psutil

## Доделать выведение всех заблоченных процессов

def get_processes(block_list=[]):

    processes = []
    for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']), 
                       key=lambda x: x.info['cpu_percent'], 
                       reverse=True):
        try:
            if proc.info['name'] in block_list:
                processes.append([
                    proc.info['pid'], 
                    proc.info['name'], 
                    f"{proc.info['cpu_percent']:.2f}%", 
                    f"{proc.info['memory_percent']:.2f}%"
                ])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return processes

