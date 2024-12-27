""" ------------------------------------------------
This is the main window for the app, which connects
to other dialogs :3

ToDo:
- Input Zone:
  - [ ] Add the scrolling widget
  - [ ] Add each workout in a grid
- Output Zone:
  - [/] About button
  - [/] Graph View
  - [ ] Save plot button

PmXa, 12-2024
------------------------------------------------ """

# --------------------
# Imports
# --------------------

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget

from datetime import date
from gui.calendar import DateSelector

import utils.data_utils as du
import utils.plot_utils as pu

# --------------------
# Class definition
# --------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        raw_data = du.read_data('./test_data.csv')
        data = du.process_data(raw_data)

    # Window setup
        self.setWindowTitle("My awesome app!")
        self.setFixedSize(QSize(800,480))
    
    # Widgets
        # Input (left) zone
        input_zone = QVBoxLayout()

        date_layout = QHBoxLayout()
        self.calendar_button = QPushButton('🗓️')
        self.today_button = QPushButton('Today')
    
        file_layout = QHBoxLayout()
        self.load_file_button = QPushButton('Load File')

        # Output (right) zone
        output_zone = QVBoxLayout()

        about_layout = QHBoxLayout()
        self.about_button = QPushButton('About')

        self.plot_area = pu.QtPlot()
        self.plot_area.plot_data(data)

        save_layout = QHBoxLayout()
        self.show_data_button = QPushButton('Show Data')
        self.save_fig_button = QPushButton('Save Plot')

    # Main signals
        self.calendar_button.clicked.connect(self.select_date)
        self.today_button.pressed.connect(self.set_today)
        self.load_file_button.pressed.connect(self.load_file)

    # Widget placement
        main_layout = QHBoxLayout()
        main_layout.addLayout(input_zone)
        main_layout.addLayout(output_zone)


        input_zone.addLayout(date_layout)
        date_layout.addWidget(self.calendar_button)
        date_layout.addWidget(self.today_button)

        input_zone.addLayout(file_layout)
        file_layout.addWidget(self.load_file_button)


        output_zone.addLayout(about_layout)
        about_layout.addWidget(self.about_button)

        output_zone.addWidget(self.plot_area)

        output_zone.addLayout(save_layout)
        save_layout.addWidget(self.show_data_button)
        save_layout.addWidget(self.save_fig_button)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    # --> Methods

    def set_today(self):
        today = date.today().strftime("%Y-%m-%d")
        self.today_button.setText(today)

    def select_date(self):
        calendar = DateSelector()
        calendar.exec()
        self.today_button.setText(calendar.date)

    def load_file():
        ...