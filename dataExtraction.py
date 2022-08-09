import requests
import json
import csv
from datetime import date
import time

import schedule as schedule

url = 'insert api url here'


def pull(download_url):
    response = requests.get(download_url)
    data = response.text
    js = json.loads(data)
    return js


# Writing into the file every first of the month

def my_file():
    if date.today().day != 1:
        return
    else:
        fields = ['Column Names']

        f = open('fileName.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(fields)

        js = pull(url)
        n = len(js)

        for i in range(n):
            writer.writerow(js[i])

    f.close()


my_file()

# For Automating the Data Extraction Process

schedule.every().day.at("00:00").do(my_file)

while True:
    schedule.run_pending()
    time.sleep(1)
