import pywhatkit
import schedule
import time
import datetime
import requests
import json

def job():
    now  = datetime.datetime.now()
    pywhatkit.sendwhatmsg("+6285326207574", "I'am phyton", 12, 7)

job()
schedule.every(3).minutes.do(job)
