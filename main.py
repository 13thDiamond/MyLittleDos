import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox

# Funktionen zum Laden und Speichern von Aufgaben in einer JSON-Datei
def load_tasks_from_json(json_file_path):
    try:
        with open(json_file_path, "r") as json_file:
            tasks = json.load(json_file)
            return tasks
    except FileNotFoundError:
        return []

def save_tasks_to_json(tasks, json_file_path):
    with open(json_file_path, "w") as json_file:
        json.dump(tasks, json_file)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.delete_button = QPushButton("Delete Task")
        self.task_list = QListWidget()
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.task_list)
        
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.del_selected_task)
        
        # Absoluter Pfad zur JSON-Datei im Unterordner "data"
        base_folder_path = os.getcwd()
        data_folder_path = os.path.join(base_folder_path, "data")
        self.json_file_path = os.path.join(data_folder_path, "tasks_archive.json")
        
        # Überprüfen, ob der Datenordner existiert, andernfalls erstellen
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)
        
        # Überprüfen, ob die JSON-Datei existiert, andernfalls eine leere Liste initialisieren
        if not os.path.exists(self.json_file_path):
            self.tasks = []
        else:
            # Laden der Aufgaben aus der JSON-Datei
            self.tasks = load_tasks_from_json(self.json_file_path)
            # Anzeigen der geladenen Aufgaben in der Liste
            for task in self.tasks:
                self.task_list.addItem(task["title"])

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append({"title": task, "status": "In Work"})
            self.task_list.addItem(task)
            self.input_field.clear()
            self.save_tasks_to_json()  # Speichern Sie die Aufgaben in der JSON-Datei

    def del_selected_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.task_list.row(item)
                self.tasks[index]["status"] = "Done"
                self.task_list.takeItem(index)
            self.save_tasks_to_json()  # Speichern Sie die Aufgaben in der JSON-Datei

    def save_tasks_to_json(self):
        save_tasks_to_json(self.tasks, self.json_file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
