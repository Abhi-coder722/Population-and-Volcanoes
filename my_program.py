import time 
import os
import pandas
while True:
    if os.path.exists('files/temp_today.csv'):
        data=pandas.read_csv('files/temp_today.csv')
        print(data.mean()["st2"])
    else:
        print('The file doesnot exist .')
    time.sleep(10)
