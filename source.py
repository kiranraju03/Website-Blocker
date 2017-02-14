import time
from datetime import datetime as dt

host_file="hosts"

redirect="127.0.0.1"
website_list=["www.python.org","python.org"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 20)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 21):
        print("dont open")
    else:
        print("can open links")
time.sleep(5)    
