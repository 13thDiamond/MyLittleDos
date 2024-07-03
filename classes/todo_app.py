# class/todo_app.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMainWindow
from PyQt6.QtCore import Qt
from task_listener import load_tasks_from_json, save_tasks_to_json
from datetime import datetime
from .list_window import ListWindow

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        self.input_field = QLineEdit()
        
        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.setObjectName("TaskButton")

        self.add_list_button = QPushButton("Add List")
        self.add_list_button.setObjectName("addListButton")

        self.delete_button = QPushButton("Delete Button")
        self.delete_button.setObjectName("deleteButton")

        self.task_list = QListWidget()
        
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_task_button)
        button_layout.addWidget(self.add_list_button)
        button_layout.addWidget(self.delete_button)
        
        self.layout.addLayout(button_layout)
        
        self.add_task_button.clicked.connect(self.add_task)
        self.add_list_button.clicked.connect(self.add_list)
        self.delete_button.clicked.connect(self.del_selected_task)
        self.task_list.itemDoubleClicked.connect(self.open_list)

        self.tasks = load_tasks_from_json()
        self.update_task_list()

    def add_task(self):
        task_title = self.input_field.text()
        if task_title:
            new_task = {
                "title": task_title,
                "status": "In Work",
                "type": "task",
                "timestamp": datetime.now().isoformat(),
                "closed_at": None
            }
            self.tasks.append(new_task)
            self.update_task_list()
            self.input_field.clear()
            save_tasks_to_json(self.tasks)

    def add_list(self):
        list_title = self.input_field.text()
        if list_title:
            new_list = {
                "title": list_title,
                "status": "In Work",
                "type": "list",
                "timestamp": datetime.now().isoformat(),
                "closed_at": None,
                "items": []
            }
            self.tasks.append(new_list)
            self.update_task_list()
            self.input_field.clear()
            save_tasks_to_json(self.tasks)

    def del_selected_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.task_list.row(item)
                self.tasks[index]["status"] = "Done"
                self.tasks[index]["closed_at"] = datetime.now().isoformat()
                self.task_list.takeItem(index)
            save_tasks_to_json(self.tasks)
 
    def open_list(self, item):
        index = self.task_list.row(item)
        if self.tasks[index]["type"] == "list":
            self.list_window = ListWindow(self.tasks[index], self.tasks)
            self.list_window.show()

    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            if task["status"] == "In Work":
                self.task_list.addItem(task["title"])
