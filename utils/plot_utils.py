from PyQt5 import QtCore

import pandas as pd
import pyqtgraph as pg

class QtPlot(pg.PlotWidget):
    def __init__(self):
        super().__init__()

        # Configure the plot
        self.setBackground("w")
        self.showGrid(x=True, y=True)

        self.setLabel("left", "Progress (%)", size="18pt")
        self.setLabel("bottom", "Days", size="18pt")
    
    def plot_data(self, processed_data: pd.DataFrame) -> None:
        """ --------------------------------------------
        Plot the results! 😁
        -------------------------------------------- """
        # Data

        x_data = processed_data.loc[1:, "days"].reset_index(drop=True)
        y_data = processed_data.loc[1:, "progress"].reset_index(drop=True)

        # Plot

        self.addItem(pg.InfiniteLine(pos=0,
                                     angle=90,
                                     pen=pg.mkPen(color="k", width=2)))
        
        self.addItem(pg.InfiniteLine(pos=0,
                                     angle=0,
                                     pen=pg.mkPen(color="k", width=2)))

        self.addItem(pg.InfiniteLine(pos=100,
                                     angle=0,
                                     pen=pg.mkPen(color="r", width=2, style=pg.QtCore.Qt.DashLine)))
        

        self.plot(x_data, y_data,
                  pen=pg.mkPen(color="b", width=2),
                  symbol="o", symbolBrush="k")