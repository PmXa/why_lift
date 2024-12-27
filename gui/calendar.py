""" ------------------------------------------------
This is the window for selecting the date of
the registry.

ToDo:
- [ ] Highlight dates with data from the file
- [ ] If there is no registry for the date, make one

PmXa, 12-2024
------------------------------------------------ """

# --------------------
# Imports
# --------------------

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QCalendarWidget, QVBoxLayout

# --------------------
# Class definition
# --------------------

class DateSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Select a date:')
    
    # Widgets
        self.calendar = QCalendarWidget(self)
        
    # Signals
        self.calendar.clicked[QDate].connect(self.select_date)

    # Placement
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

    # --> Methods

    def select_date(self, qDate):
        self.date = qDate.toString("yyyy-MM-dd")
        self.close()