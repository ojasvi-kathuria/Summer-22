from time import time
import pandas as pd  
import numpy as np
from datetime import datetime
from mainwindow import upload_file


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
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
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
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        arr_ut.append(diff_in_minutes)

    used_time = sum(arr_ut)
    return("online time of device: " + str(used_time))

usedtime()
