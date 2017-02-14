import time
from datetime import datetime as dt

host_file="hosts"

redirect="127.0.0.1"
website_list=["www.python.org","python.org"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 20)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 21):
        print("Should not access the website")
        with open(host_file,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")
                    
    else:
        print("can open links")
time.sleep(5)
