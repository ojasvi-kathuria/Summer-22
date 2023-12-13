import tkinter as tk
from tkinter import Frame, ttk
import pandas as pd
from tkinter import filedialog
from tkinter.filedialog import askopenfile
df = pd.DataFrame()

from usedtime import *
from runtime import *
from engperhour import *
from energytrend1 import *
from roomhumidity import *
from roomtemp import *



second=tk.Tk()
def create_main_window():
    second.destroy()

    def algo(df):
        u_ton = usedtime()
        r_time = runtime()[0]
        e_day = energy()
        return(u_ton, "runtime: " + str(r_time), "energy per day: " +str(e_day))

    def algo1(df):
        trend = energy_trend()
        rh = humidity_room()
        rt = temp_room()
        return(trend, "humidity issue: " +str(rh), "temp issue: " +str(rt))

    def upload_file():
        
        global df
        f_types = [('CSV files',"*.csv"),('All',"*.*")]
        file = filedialog.askopenfilename(filetypes=f_types)
        df=pd.read_csv(file) # create DataFrame
        return df

    def analyse():
        global df
        global str2
        global str3
        str2 = algo(df)
        str3 = algo1(df)
        second_window()
        root.destroy()

    def second_window():
        global second
        root.destroy()
        second = tk.Tk()
        second.title('Result')
        second.geometry("800x500")
        t1= tk.Text(second, width = 100, height=13)
        t1.grid(row = 0, column = 0, padx =5)
        t1.insert(tk.END, str2)

        t2= tk.Text(second, width = 100, height=15)
        t2.grid(row = 1, column = 0, padx =5)
        t2.insert(tk.END, str3)

        b3= tk.Button(second, text='Go Back', width= 50, command= lambda:create_main_window())
        b3.grid(row= 2, column =0)

    # root window
    root = tk.Tk()
    root.title('Living Things')
    root.geometry("800x500")

    llt = tk.Label(root, text = "Living Things")
    llt.place(x= 10, y=10)

    l1 = tk.Label(root, text = "MET-D Algorithm Simulator", font=("Arial", 25))
    l1.place(x= 200, y=100)

    b1 = tk.Button(root, text='Browse', width=50,command = lambda:upload_file())
    b1.place(x=220, y = 200)

    b2 = tk.Button(root, text='Analyse and process', width=50,command = lambda: analyse())
    b2.place(x=220, y = 250) 

    root.mainloop()


    
if __name__ == "__main__":
    create_main_window()
