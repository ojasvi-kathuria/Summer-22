from datetime import datetime
import pandas as pd
import numpy as np
from datetime import timedelta

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
    bsp = power[0] 
    band_time = []*size 

    for i in range(1, n):
    
        date_0 = bst
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
        bst1 = datetime.strptime(date_0, date_format_str)
        bet1 = bst1 + timedelta(hours = 1)
        bet = bet1.strftime('%d/%m/%Y %H:%M:%S.%f')

        date_1 = time_array[i]
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
        start = datetime.strptime(date_0, date_format_str)
        end =   datetime.strptime(date_1, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = end - start
        # Get the interval in minutes
        diff_in_minutes = diff.total_seconds() / 60
        
        if (diff_in_minutes>60):
            bst = bet
            arr_eng.append(power[i-1]-bsp)
            band_time.append(bst)
            bsp = power[i]
        
    
    energy_day = 0

    for i in range(0, len(arr_eng)):
        energy_day = energy_day +arr_eng[i]

    return(energy_day)
        

energy()
        

