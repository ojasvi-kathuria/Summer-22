from datetime import datetime
from platform import java_ver
import pandas as pd
import numpy as np
from datetime import timedelta
from runtime import *
from mainwindow import *

def humidity_room():
    lst1 = runtime()[1]
    time_array = df['timestamp'].to_numpy()
    humidity = df['humidity'].to_numpy()
    j = 0
    for i in range(0, len(lst1)):
        date_0 = lst1[j]
        date_1 = time_array[i]
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
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



