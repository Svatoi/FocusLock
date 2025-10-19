from app.utils import logger


def user_interface(bl):
    
    process=input('Enter a list of process wich you like to ban, separated by commas: ')
    # sites=input('\nEnter a list of sites wich you like to ban, separated by commas: ') This will work when I make own browser extensions
    
    # list_of_blocked_websites = ['https://' + x.strip().lower() for x in sites.split(',')]
    list_of_blocked_processes = [x.strip().lower() + '.exe' for x in process.split(',')]
    
    # bl.add_processes(list_of_blocked_websites)
    bl.add_processes(list_of_blocked_processes)
    
    remove_process=input('\nDo you want to remove one of your blocked processes?(Yes/No): ')
    if remove_process == 'No':
        logger.info("Idi nahur")
    if remove_process == 'Yes':
        list_process=input(f"\nWhat process do you want to remove?({list_of_blocked_processes}):")
        process = [x.strip().lower() + '.exe' for x in list_process.split(',')]
        bl.remove_processes(process)
        
    add_process=input('\nDo you want to add some processes to block list?(Yes/No): ')
    if add_process == 'No':
        logger.info("Dyra")
    if add_process == 'Yes':
        process=input(f"What process do you want to add?({list_of_blocked_processes}):")
        bl.add_processes(process)