import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
from task_listener import load_tasks_from_json, save_tasks_to_json

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
        

        json_folder_path = os.path.join(os.path.dirname(__file__), "data")
        json_file_path = os.path.join(os.path.dirname(__file__), "task_list.json")
        
        if not self.load_tasks_from_json(json_file_path):
            QMessageBox.critical(self, "Fehler", "Die Datei task_list.json wurde nicht gefunden!")

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append({"title": task, "status": "In Work"})
            self.task_list.addItem(task)
            self.input_field.clear()
            self.save_tasks_to_json()

    def del_selected_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.task_list.row(item)
                del self.tasks[index]
                self.task_list.takeItem(index)
            self.save_tasks_to_json(json_file_path)

    def load_tasks_from_json(self, json_file_path):
        self.tasks = load_tasks_from_json(json_file_path)
        for task in self.tasks:
            self.task_list.addItem(task["title"])
        return bool(self.tasks)

    def save_tasks_to_json(self):
        save_tasks_to_json(self.tasks, json_file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())