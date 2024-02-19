import sys
from PyQt6.QtWidgets import QApplication
from gui import ToDoApp

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=ToDoApp()
    window.show()
    sys.exit(app.exec())