from datetime import datetime, timedelta
from task_listener import load_tasks_from_json, save_tasks_to_json

def load_tasks():
    tasks = load_tasks_from_json()
    tasks = remove_old_done_tasks(tasks)
    return tasks

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
    reorder_tasks(tasks)

def reorder_tasks(tasks):
    tasks.sort(key=lambda task: (task["status"] == "Done", task["timestamp"]))
    save_tasks(tasks)

def update_task_list(tasks):
    return [task for task in tasks if task["status"] == "In Work"]

def remove_old_done_tasks(tasks, days=30):
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=days)
    
    tasks_to_keep = []
    for task in tasks:
        if task["status"] == "Done":
            closed_at = datetime.fromisoformat(task["closed_at"])
            if closed_at >= threshold_time:
                tasks_to_keep.append(task)
        else:
            tasks_to_keep.append(task)
    
    return tasks_to_keep

def cleanup_old_tasks():
    tasks = load_tasks_from_json()
    tasks = remove_old_done_tasks(tasks)
    save_tasks(tasks)
