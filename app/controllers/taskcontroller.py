from app.models import Task
from app.database import session

from app.utils import logger

class TaskController:
    @staticmethod
    def create_task(name: str, description: str, score: int, user_id: int):
        task = Task(name=name, description=description, score=score, user_id=user_id)
        task.save()
        task.refresh()
        logger.info(f"Task was add: {task}")
    
    @staticmethod
    def get_tasks_by_user_id(user_id: int):
        tasks = session.query(Task).filter(user_id == user_id).all()
        
        if not tasks:
            logger.info("User don't have any task")
            return print("You don't have any tasks")
        
        list_name_of_tasks = []
        for i, task in enumerate(tasks, start=0):
            name = '{} {}'.format(i + 1, task.name)
            list_name_of_tasks.append(name)
            
        logger.info(f"The user has tasks such as: {list_name_of_tasks}")
        return list_name_of_tasks
    
    @staticmethod
    def is_done_task(user_id: int):
        tasks = session.query(Task).filter(Task.user_id == user_id).all()
        return any(task.is_done for task in tasks)
    
    @staticmethod
    def edit_tasks(user_id: int, task_name: str):
        attribute_to_update = input("What do you want to edit?(Write the number): \n1. Name \n2. Description \n")

        task = session.query(Task).filter(Task.user_id == user_id, Task.name == task_name).first()
        
        if attribute_to_update == "1":
            updated_value = input(f"(Current: '{task_name}'): Write new name \n>> ")

            session.query(Task).filter(Task.user_id == user_id, Task.name == task_name).update({"name": updated_value})
            
            session.commit()
            
        if attribute_to_update == "2":
            updated_value = input(f"(Current: '{task.description}'): Write new description \n>> ")
            
            session.query(Task).filter(Task.user_id == user_id, Task.name == task_name).update({"description": updated_value})
            
            session.commit()
            
        
            