from datetime import datetime
from task_listener import load_tasks_from_json, save_tasks_to_json

def load_tasks():
    return load_tasks_from_json()

def save_tasks(tasks):
    save_tasks_to_json(tasks)

def add_task(tasks, task_title):
    if task_title:
        new_task ={
            "title": task_title,
            "status": "In Work",
            "type": "task",
            "timestamp": datetime.now().isoformat(),
            "closed_at": None
        }
        tasks.append(new_task)
        save_tasks(tasks)

def add_list(tasks, list_title):
    if list_title:
        new_list = {
            "title": list_title,
            "status": "In Work",
            "type": "list",
            "timestamp": datetime.now().isoformat(),
            "closed_at": None,
            "items": []
        }
        tasks.append(new_list)
        save_tasks(tasks)

def delete_task(tasks, index):
    tasks[index]["status"]="Done"
    tasks[index]["closed_at"]=datetime.now().isoformat()
    save_tasks(tasks)

def reorder_tasks(tasks):
    tasks.sort(key=lambda task: (task["status"] == "Done", task["timestamp"]))
    save_tasks(tasks)

def update_task_list(tasks):
    return [task for task in tasks if task["status"] == "In Work"]