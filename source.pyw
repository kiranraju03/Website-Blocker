import time
from datetime import datetime as dt

#host_file=r"F:\Codes\Website_Blocker\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"
website_list=["www.python.org","python.org"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 19)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 23):
        print("Should not access the website")
        with open(host_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")

    else:
        print("Can open links")
        with open(host_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
time.sleep(5)
