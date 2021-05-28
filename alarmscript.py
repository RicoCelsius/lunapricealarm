
import sched
import threading
import time
import schedule
import json
from pycoingecko import CoinGeckoAPI
from playsound import playsound
cg = CoinGeckoAPI()
scheduler = sched.scheduler(time.time, time.sleep)
lunepriceglobal = str(cg.get_price(ids='terra-luna', vs_currencies='usd')['terra-luna']['usd'])






print("Please specify at which LUNA price you would like to hear an alarm.")
print("Current price:"+ lunepriceglobal)
alarmprice = input()

def resetConnection():
    print("Connection was lost, resetting connection in 30 seconds.")
    time.sleep(30)

def task():
    print ("Checking LUNA Price...")
    try: 
        data = cg.get_price(ids='terra-luna', vs_currencies='usd')
        lunaprice = data['terra-luna']['usd']
        print("Current price:" + str(lunaprice))
        if lunaprice <= float(alarmprice):
            playsound('audio.mp3')
            print("ALARM please deposit more collateral or repay your loan!")
        else:
            print("Everything fine, have a great day/night")
    except:
        resetConnection()
    return ...


schedule.every(5).seconds.do(task)  # Runs every 5 seconds


    


while True:
    schedule.run_pending()
    time.sleep(1)