import os
import json

def load_tasks_from_json():
    json_file_path = os.path.join("data", "tasks_archive.json")
    if os.path.exists(json_file_path):
        try:

            with open(json_file_path, "r") as json_file:
                tasks = json.load(json_file)
                in_work_tasks = [task for task in tasks if task.get("status")== "In Work"]
                return in_work_tasks
        except FileNotFoundError:    
                return []
    
def save_tasks_to_json(tasks):
    json_file_path = os.path.join("data", "tasks_archive.json")
    ensure_data_folder_and_json_exists()
    with open(json_file_path, "w") as json_file:
        json.dump(tasks, json_file, indent=4)

def ensure_data_folder_and_json_exists():
    data_folder_path = os.path.join("data")
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)
    json_file_path = os.path.join("data", "tasks_archive.json")
    if not os.path.exists(json_file_path):
        with open(json_file_path, "w") as json_file:
            json.dump([], json_file)