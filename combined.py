import tkinter as tk
from tkinter import Frame, ttk
import pandas as pd
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from datetime import datetime
from time import time
from platform import java_ver
from datetime import timedelta
from xmlrpc.client import boolean
df = pd.DataFrame()

def usedtime():
    size = 99999
    ping_rate = 5
    time_array = df['timestamp'].to_numpy()
    type = df['type'].to_numpy()
    n = len(time_array)

    arr_ts = [] * size
    arr_ts.append(time_array[0])

    i = 0
    for i in range (n-1): 
        date_0 = time_array[i]
        date_1 = time_array[i+1]
        date_format_str = '%d/%m/%Y %H:%M:%S'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        if(diff_in_minutes>12 or diff_in_minutes<2):
            arr_ts.append(time_array[i])
            arr_ts.append(time_array[i+1])
        
    if(type[n-1]== 'dp'):
        arr_ts.append(time_array[n-1])


    n1 = len(arr_ts)
    arr_ut = []*size
    for i in range (0,n1-1,2):
        date_0 = arr_ts[i]
        date_1 = arr_ts[i+1]
        date_format_str = '%d/%m/%Y %H:%M:%S'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        arr_ut.append(diff_in_minutes)

    used_time = sum(arr_ut)
    return("online time of device: " + str(used_time))
def humidity_room():

    lst1 = runtime()[1]
    time_array = df['timestamp'].to_numpy()
    humidity = df['humidity'].to_numpy()
    j = 0
    for i in range(0, len(lst1)):
        date_0 = lst1[j]
        date_1 = time_array[i]
        date_format_str = '%d/%m/%Y %H:%M:%S'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        if(diff_in_minutes>60):
            if(humidity[i]>65):
                return("Cooling capacity not up to mark, can't maintaine RH")
            j = j+1
def temp_room():

    time_array = df['timestamp'].to_numpy()
    temp = df['temp'].to_numpy()
    j = 0
    lst1 = runtime()[1]
    for i in range(0, len(lst1)):
        date_0 = lst1[j]
        date_1 = time_array[i]
        date_format_str = '%d/%m/%Y %H:%M:%S'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        if(diff_in_minutes>60):
            if(temp[i]>30):
                print("Cooling capacity not up to mark")
            j = j+1
def runtime():
    size = 99999
    p0 = 500
    lst1 = []*size
    lst2 = []*size
    time_array = df['timestamp'].to_numpy()
    power = df['power'].to_numpy()
    type = df['type'].to_numpy()
    n = len(power)
    state = 0
    
    for i in range(0, n):
        if(state ==0):
            if(power[i]<p0):
                state = 0
            else:
                state = 1
                lst1.append(time_array[i])
            
        if(state == 1):
            if(power[i]>p0):
                state=1
            else:
                state = 0
                lst2.append(time_array[i])
                
     
    if(type[n-1]== 'dp'):
        lst2.append(time_array[n-1])  
    band_list = []*size
    if(len(lst1)==len(lst2)):
        for i in range(0,len(lst1)):
            date_0 = lst1[i]
            date_1 = lst2[i]
            date_format_str = '%d/%m/%Y %H:%M:%S'
            start = datetime.strptime(date_0, date_format_str)
            end =   datetime.strptime(date_1, date_format_str)
            # Get interval between two datetimes as timedelta object
            diff = end - start
            # Get the interval in minutes
            diff_in_minutes = diff.total_seconds() / 60
            band_list.append(diff_in_minutes)

    elif(len(lst1)>len(lst2)):
        band_list_len = len(lst1)-len(lst2)
        for i in range(0,len(lst2)):
            date_0 = lst1[i]
            date_1 = lst2[i]
            date_format_str = '%d/%m/%Y %H:%M:%S'
            start = datetime.strptime(date_0, date_format_str)
            end =   datetime.strptime(date_1, date_format_str)
            # Get interval between two datetimes as timedelta object
            diff = end - start
            # Get the interval in minutes
            diff_in_minutes = diff.total_seconds() / 60
            band_list.append(diff_in_minutes)

        for j in range(0,len(lst1)-len(lst2)):
            band_list.append(lst1[j])
    else:
        band_list_len = len(lst2)-len(lst1)
        for i in range(0,len(lst1)):
            date_0 = lst1[i]
            date_1 = lst2[i]
            date_format_str = '%d/%m/%Y %H:%M:%S'
            start = datetime.strptime(date_0, date_format_str)
            end =   datetime.strptime(date_1, date_format_str)
            # Get interval between two datetimes as timedelta object
            diff = end - start
            # Get the interval in minutes
            diff_in_minutes = diff.total_seconds() / 60
            band_list.append(diff_in_minutes)

        for j in range(0,len(lst2)-len(lst1)):
            band_list.append(lst2[j])

    runtime_value = sum(band_list)
    return(runtime_value, lst1, lst2)
def energy():
    energy = df['current_kwh'].to_numpy()
    size = 99999
    arr_eng = [] * size
    time_array = df['timestamp'].to_numpy()
    power = df['power'].to_numpy()
    n = len(time_array)
    date_0 = time_array[0]
    bst = date_0

    #bet1 =  bst1 + timedelta(hours = 1)
    #bet = bet1.strftime('%d/%m/%Y %H:%M:%S.%f')
    bsp = energy[0] 
    band_time = []*size 

    for i in range(1, n):
    
        date_0 = bst
        date_format_str = '%d/%m/%Y %H:%M:%S'
        bst1 = datetime.strptime(date_0, date_format_str)
        bet1 = bst1 + timedelta(hours = 1)
        bet = bet1.strftime('%d/%m/%Y %H:%M:%S')

        date_1 = time_array[i]
        date_format_str = '%d/%m/%Y %H:%M:%S'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        
        if (diff_in_minutes>60):
            bst = bet
            arr_eng.append(energy[i-1]-bsp)
            band_time.append(bst)
            bsp = energy[i]
        
    
    energy_day = 0
    print(arr_eng)

    for i in range(0, len(arr_eng)):
        energy_day = energy_day +arr_eng[i]

    return(energy_day)
def energy_trend():

    #energy_day = energy()
    t_run = runtime()[0]
    print(t_run)
    energy_day = [2,4, 10, 15, 20]
    count = 0
    for i in range(0, len(energy_day)-1):
        if(energy_day[i+1]>1.1*energy_day[i]):
            count = count+1
            if(count == 4):
                if(energy_day[i]/energy_day[0]>1.5):
                    return("Rule 1 is triggered")

        elif(energy_day[i+1]<0.9*energy_day[i]):
            count = 0


    count1 = 0
    for i in range(0, len(energy_day)-1):
        if(energy_day[i+1]/int(t_run)>1.1*energy_day[i]/int(t_run)):
            count1 = count1+1
            if(count1 == 2):
                if(energy_day[i]/energy_day[0]>1.2):
                    return("Rule 2 is triggered")

        elif(energy_day[i+1]/int(t_run)<0.9*energy_day[i]/int(t_run)):
            count1 = 0

    count2 = 0
    for i in range(0, len(energy_day)-1):
        if(energy_day[i+1]<0.9*energy_day[i]):
            count2 = count2 +1
            if(count2 == 1):
                if(energy_day[i]/energy_day[0]<0.8):
                    return("Rule 3 is triggered")

        elif(1.1*energy_day[i]<energy_day[i+1]):
            count2 = 0


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
