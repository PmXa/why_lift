""" ------------------------------------------------
This is the main window for the app, which connects
to other dialogs :3

ToDo:
- Input Zone:
  - [x] Add the scrolling widget
  - [x] Add each workout in a grid
    - [ ] Color the total labels
  - [/] Make LineEdits modify the DataFrame
- Output Zone:
  - [ ] About button
  - [/] Graph View
  - [X] Save plot button

-> The load_date method should load the last session
    and modify the today_button's text to the
    currently selected_date. Then, the manual label
    from line 69 can be deleted.

PmXa, 12-2024
------------------------------------------------ """

# --------------------
# Imports
# --------------------

from PyQt5.QtCore import Qt, QSize
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

        raw_data, self.workout_names = du.read_data('./test_data.csv')
        self.data = du.process_data(raw_data, self.workout_names)
        self.selected_date = self.data['Date'].iloc[-1].date()

    # Window setup
        self.setWindowTitle("My awesome app!")
        self.setFixedSize(QSize(800,480))
    
    # Widgets
        # Input (left) zone
        input_zone = QVBoxLayout()

        date_layout = QHBoxLayout()
        self.calendar_button = QPushButton('🗓️')
        self.today_button = QPushButton(str(self.selected_date))
    
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setFixedWidth(200)
        self.scroll_container = QWidget()
        self.input_layout = QVBoxLayout(self.scroll_container)
        self.generate_entries(self.data)

        file_layout = QHBoxLayout()
        self.load_file_button = QPushButton('Load File')

        # Output (right) zone
        output_zone = QVBoxLayout()

        about_layout = QHBoxLayout()
        self.about_button = QPushButton('About')

        self.plot_area = pu.QtPlot()
        self.plot_area.plot_data(self.data)

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

    # --> Post-UI Code Execution

    """ 🚧 🚧 🚧
    This is a good place to include the load_date method call, since it requires UI modification, and can use the self.input_LineEdits dictionary to do so!
    """

    # --> Methods

    def set_today(self) -> None:
        """
        This function:
        0. Updates the selected_date property
        1. Creates a new row with today's date
        2. Updates the button label
        """
        today = date.today().strftime("%Y-%m-%d")
        self.selected_date = pd.to_datetime(today)

        # Check if the current date exists to avoid duplicates!
        if any(self.data['Date'] == self.selected_date):
            self.load_session(self.data, today)
        else:
            self.data = self.create_session(self.data, self.selected_date)

        self.today_button.setText(today)
        self.plot_area.plot_data(self.data)


    def select_date(self):
        """
        This function:
        - [ ] Selects a date from a calendar widget
        - [ ] Sets it as the self.selected_date
        - [ ] Distinguishes aming dates with and without a session register
        - [?] Allows to modify previous sessions
        """
        calendar = DateSelector()
        calendar.exec()
        self.today_button.setText(calendar.date)
        # ToDo: Set self.selected_date


    def load_session(self, data: pd.DataFrame, date) -> None:
        """
        This function displays a previous session selected from the calendar window and allows for its modification.
        """


    def create_session(self, data: pd.DataFrame, date) -> pd.DataFrame:
        """
        This function creates a new row in the DataFrame prepopulated with zeros.
        """
        
        new_row = {column: (date if column == 'Date' else [0]) for column in data.columns.values}
        new_row = pd.DataFrame(new_row)
        new_row["Date"] = pd.to_datetime(new_row["Date"])

        new_data = pd.concat([data, new_row], ignore_index=True)
        return du.process_data(new_data, self.workout_names)


    def generate_entries(self, data: pd.DataFrame) -> None:
        """
        This function reads the different exercises listed in the csv file and generates a field for every one of them. 
        """
        self.input_LineEdits = {}

        for entry in self.workout_names:
            entry_row_layout = QHBoxLayout()

            exercise_title = QLabel(f"{entry}".title())
            exercise_title.setWordWrap(True)
            exercise_title.setFixedWidth(96)
            entry_row_layout.addWidget(exercise_title)

            rep_input = QLineEdit()
            last_rep = data[entry].iloc[-1]
            rep_input.setPlaceholderText(str(last_rep))
            rep_input.setFixedWidth(36)
            rep_input.setAlignment(Qt.AlignmentFlag.AlignRight)
            entry_row_layout.addWidget(rep_input)

            target_rep = data[entry][0]
            target_rep_label = QLabel(f"/{target_rep}")
            entry_row_layout.addWidget(target_rep_label)

            rep_input.textChanged.connect(lambda text, id=entry: self.input_rep_changed(text, id))

            self.input_LineEdits[entry] = rep_input
            self.input_layout.addLayout(entry_row_layout)

        # Añadir un espacio al final para estética
        self.input_layout.addStretch()


    def input_rep_changed(self, reps: str, id: str) -> None:
        index = (self.data['Date'] == pd.to_datetime(self.selected_date))
        self.data.loc[index, id] = int(reps)

        self.data = du.process_data(self.data, self.workout_names)
        self.plot_area.update_plot(self.data)


    def load_file():
        ...