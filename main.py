import pywhatkit
import schedule
import time
import datetime
import requests
import json

def job():
    now  = datetime.datetime.now()
    pywhatkit.sendwhatmsg("+", "I'am phyton", 12, 7)

job()
schedule.every(3).minutes.do(job)
