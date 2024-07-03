# class/list_window.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from datetime import datetime
from task_listener import save_tasks_to_json

class ListWindow(QWidget):
    def __init__(self, list_item, parent_tasks):
        super().__init__()
        self.setWindowTitle(list_item["title"])
        self.setGeometry(150, 150, 600, 400)

        self.list_item = list_item
        self.parent_tasks = parent_tasks  # Reference to the parent task
        self.layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.add_subtask_button = QPushButton("Add Subtask")
        self.add_subtask_button.setObjectName("addSubtaskbutton")

        self.del_subtask_button = QPushButton("Delete Subtask")
        self.del_subtask_button.setObjectName("deleteSubtaskbutton")


        self.subtask_list = QListWidget()

        self.layout.addWidget(self.subtask_list)
        self.layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_subtask_button)
        button_layout.addStretch()
        button_layout.addWidget(self.del_subtask_button)

        self.layout.addLayout(button_layout)

        self.add_subtask_button.clicked.connect(self.add_subtask)
        self.del_subtask_button.clicked.connect(self.del_subtask)
        self.update_subtask_list()
        self.setLayout(self.layout)

    def add_subtask(self):
        subtask_title = self.input_field.text()
        if subtask_title:
            new_subtask = {
                "title": subtask_title,
                "status": "In Work",
                "type": "task",
                "timestamp": datetime.now().isoformat(),
                "closed_at": None
            }
            self.list_item["items"].append(new_subtask)
            self.update_subtask_list()
            self.input_field.clear()
            save_tasks_to_json(self.parent_tasks)  # Save to the main tasks JSON

    def del_subtask(self):
        selected_items = self.subtask_list.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.subtask_list.row(item)
                self.list_item["items"][index]["status"] = "Done"
                self.list_item["items"][index]["closed_at"] = datetime.now().isoformat()
                self.subtask_list.takeItem(index)
            save_tasks_to_json(self.parent_tasks)

    def update_subtask_list(self):
        self.subtask_list.clear()
        for subtask in self.list_item["items"]:
            if subtask["status"] == "In Work":
                self.subtask_list.addItem(subtask["title"])
