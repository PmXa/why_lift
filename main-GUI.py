""" *******************************************************
This is the main GUI file for project 'Why Lift! 💪🤔💭' :3

PmXa, 12-2024
******************************************************* """

from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from os import path

# -----------
# Entry Point
# -----------

if __name__ == '__main__':
    app = QApplication([])

# Check if there is a data file to work with
    if path.exists('./test_data.csv'):
        main_window = MainWindow()
        main_window.show()
# Otherwise load a "fresh start" version of the app (ToDo)
    else:
        print('No implemented yet!')
        raise FileNotFoundError

    app.exec()