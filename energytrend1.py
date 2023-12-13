from datetime import datetime
import pandas as pd
import numpy as np
from datetime import timedelta
from runtime import *
from engperhour import *

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


        

        
        
