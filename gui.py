from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from task_listener import load_tasks_from_json, save_tasks_to_json

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 700, 300)
        
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

        self.tasks = load_tasks_from_json()
        self.update_task_list()

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append({"title": task, "status": "In Work"})
            self.update_task_list()
            self.input_field.clear()
            save_tasks_to_json(self.tasks)

    def del_selected_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.task_list.row(item)
                self.tasks[index]["status"] = "Done"
                self.task_list.takeItem(index)
            save_tasks_to_json(self.tasks)
 
    


    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(task["title"])