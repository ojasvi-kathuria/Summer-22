from datetime import datetime
from tkinter import OFF
from xmlrpc.client import boolean
import pandas as pd
import numpy as np
from datetime import timedelta

def runtime():
    size = 99999
    p0 = 10
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
                i = i+1
        if(state == 1):
            if(power[i]>p0):
                state=1
            else:
                state = 0
                lst2.append(time_array[i])
                i = i+1
     
    if(type[n-1]== 'dp'):
        lst2.append(time_array[n-1])  
      

    band_list = []*size
    if(len(lst1)==len(lst2)):
        for i in range(0,len(lst1)):
            date_0 = lst1[i]
            date_1 = lst2[i]
            date_format_str = '%d/%m/%Y %H:%M:%S.%f'
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
            date_format_str = '%d/%m/%Y %H:%M:%S.%f'
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
            date_format_str = '%d/%m/%Y %H:%M:%S.%f'
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

runtime()