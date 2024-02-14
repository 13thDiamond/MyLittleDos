import json

def load_tasks_from_json(json_file_path):
    try:
        with open(json_file_path, "r") as json_file:
            tasks = json.load(json_file)
            return tasks
    except FileNotFoundError:
        return[]
    
def save_tasks_to_json(tasks, json_file_path):
    with open(json_file_path, "w") as json_path:
        json.dump(tasks, json_file)