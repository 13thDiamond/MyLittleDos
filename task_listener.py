import os
import json
from datetime import datetime

def load_tasks_from_json():
    ensure_data_folder_and_json_exists()
    try:
        with open("data/tasks_archive.json", "r") as json_file:
            date = json.load(json_file)
            tasks = date.get("tasks", [])
            in_work_tasks = [task for task in tasks if task.get("status")== "In Work"]
            return in_work_tasks
    except FileNotFoundError:    
        return []
    
def save_tasks_to_json(tasks):
    json_file_path = os.path.join("data", "tasks_archive.json")
    ensure_data_folder_and_json_exists()
    data = {"tasks": tasks}
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def ensure_data_folder_and_json_exists():
    data_folder_path = os.path.join("data")
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)
    json_file_path = os.path.join(data_folder_path, "tasks_archive.json")
    if not os.path.exists(json_file_path):
        with open(json_file_path, "w") as json_file:
            json.dump({"tasks":[]}, json_file)