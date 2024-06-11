import sys
from PyQt6.QtWidgets import QApplication
from classes.todo_app import ToDoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())