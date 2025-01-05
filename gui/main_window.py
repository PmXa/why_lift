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
  - [X] Save plot button

PmXa, 12-2024
------------------------------------------------ """

# --------------------
# Imports
# --------------------

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget
)

from datetime import date
from gui.calendar import DateSelector

import pandas as pd
import utils.data_utils as du
import utils.plot_utils as pu

# --------------------
# Class definition
# --------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # For debugging purposes: use extended_data.csv
        raw_data = du.read_data('./extended_data.csv')
        # raw_data = du.read_data('./test_data.csv')
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
    
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_container = QWidget()
        self.input_layout = QVBoxLayout(self.scroll_container)
        self.generate_entries(data)

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

        self.save_fig_button.pressed.connect(self.plot_area.save_plot)

    # Widget placement
        main_layout = QHBoxLayout()
        main_layout.addLayout(input_zone)
        main_layout.addLayout(output_zone)


        input_zone.addLayout(date_layout)
        date_layout.addWidget(self.calendar_button)
        date_layout.addWidget(self.today_button)

        input_zone.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_container)

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

    def generate_entries(self, data: pd.DataFrame) -> None:
        entries = data.columns.values[1:-3]

        for entry in entries:
            entry_row_layout = QHBoxLayout()

            exercise_title = QLabel(f"{entry}".title())
            entry_row_layout.addWidget(exercise_title)

            rep_input = QLineEdit()
            entry_row_layout.addWidget(rep_input)

            target_rep_label = QLabel("(Extra)")
            entry_row_layout.addWidget(target_rep_label)

            self.input_layout.addLayout(entry_row_layout)

        # Añadir un espacio al final para estética
        self.input_layout.addStretch()

    def load_file():
        ...