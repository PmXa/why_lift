""" ------------------------------------------
This script has the GUI for my Workout Tracker
PmXa, 06-2024
------------------------------------------ """

# Modules

import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog

# GUI elements

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DataFrame Viewer and Plotter")
        self.create_widgets()

    def create_widgets(self):
        # Split the main window
        self.frame_left = tk.Frame(self.root)
        self.frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Add the button to load the .xlsx file
        self.load_button = tk.Button(self.frame_left, text="Load XLSX File", command=self.load_file)
        self.load_button.pack(pady=10)
        
        # Label to display the last row of the dataframe
        self.last_row_label = tk.Label(self.frame_left, text="Last row of DataFrame will be shown here")
        self.last_row_label.pack(pady=10)
        
        # Create a matplotlib figure
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame_right)
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.pack(fill=tk.BOTH, expand=True)
        
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.df = pd.read_excel(file_path)
            self.show_last_row()
            self.plot_data()

    def show_last_row(self):
        last_row = self.df.iloc[-1]
        self.last_row_label.config(text=f"Last row:\n{last_row}")

    def plot_data(self):
        # Clear previous plot
        self.figure.clear()
        
        # Plotting the first two columns as an example
        if len(self.df.columns) >= 2:
            ax = self.figure.add_subplot(111)
            ax.plot(self.df[self.df.columns[0]], self.df[self.df.columns[1]])
            ax.set_xlabel(self.df.columns[0])
            ax.set_ylabel(self.df.columns[1])
            self.canvas.draw()

# Entry point

if __name__ == '__main__':
	root = tk.Tk()
	app = App(root)
	root.mainloop()