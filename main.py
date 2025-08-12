import sys
from PyQt6.QtWidgets import QApplication
from classes.todo_app import ToDoApp

def load_stylesheet(main_style):
    with open(main_style, "r") as file:
        main_style = file.read()
    return main_style

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    
    stylesheet = load_stylesheet("stylesmap/main_style.qss")
    app.setStyleSheet(stylesheet)

    window.show()
    sys.exit(app.exec())

    
