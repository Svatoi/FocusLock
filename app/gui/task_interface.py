from app.utils import logger
from app.models import User
import random
from app.controllers import TaskController

def task_interface(session):
    
    tasks = input('\nDo you want to add some task?(Yes/No): ')
    if tasks == 'No':
        logger.info("Dyra konch")
    if tasks == 'Yes':
        user_id = session.query(User).filter(User.id == 1).first()
        TaskController.create_task(
            name=input("Enter a name of task: "),
            description=input("Enter a description of task: "),
            score=random.randrange(1, 100),
            user_id=user_id.id
        )
        
    edit_tasks = input("\nDo you want to edit your task?(Yes/No): ")
    if edit_tasks == 'No':
        logger.info("Dyra konch 2")
    if edit_tasks == 'Yes':
        user_id = session.query(User).filter(User.id == 1).first()   
        task_name = TaskController.get_tasks_by_user_id(user_id=user_id.id)
        logger.info(f"The user has the following tasks: {task_name}")
        
        print(f"You have such tasks as: {task_name}")
        
        editable_task_name = input("What task do you want to edit?(Input a name of task): \n>> ")
        logger.info(f"User want to edit {editable_task_name}")
        TaskController.edit_tasks(user_id=user_id.id, task_name=editable_task_name)