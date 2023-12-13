import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from mainwindow import create_main_window

df = pd.DataFrame()

def second_window():

    for widget in frame.winfo_children():
        widget.destroy()

    t1= tk.Text(root, width = 100, height=5)
    t1.grid(row = 0, column = 0, padx =5)
    t1.insert(tk.END, str2)

    t2= tk.Text(root, width = 100, height=5)
    t2.grid(row = 1, column = 0, padx =5)
    t2.insert(tk.END, str3)

if __name__ == "__main__":
    second_window()

