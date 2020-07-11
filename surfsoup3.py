import time
import magicseaweed
#import pandas as pd
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def unique(list1):
    #initialize a null list
    uniqueList = []

    for x in list1:
        if x not in uniqueList:
            uniqueList.append(x)

    print(uniqueList)
    return(uniqueList)
 
    
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

api_key = "54581012c82ad9250600ea521bf8dd24" 
clam_id = 4709
#martinique_id = 371

clam_forecast = magicseaweed.MSW_Forecast(api_key, clam_id)
#clam_now = clam_forecast.get_current()
#print(clam_now.attrs)

clam_future = clam_forecast.get_future()
print(clam_future.summary)

data = pd.DataFrame() 

for forecast in clam_future.data:
    forecastTime = time.ctime(forecast.d['localTimestamp'])
    forecastDOW = forecastTime.split(' ', 1)[0]
    print(forecastTime, ':', forecast.d['solidRating'])
#   print(forecast.get_chart_url('swell'))
    data = data.append(pd.DataFrame({'date' : forecastTime,
        'weekday': forecastDOW, 
        'Rating' : forecast.d['solidRating']}, index = [0]))

print(data.head())

bestrating=[]
for day in pd.unique(data['weekday']):
    print(day, "======")
    print(data[data['weekday'] == day])
    maxForDay = data[data['weekday'] == day].max()
    print(maxForDay)
    bestrating.append(maxForDay['Rating'])
#    bestrating[day]

print(bestrating)
#print(bestrating

gpios = [17,18,22,23,9,25]

for i in gpios:
    print("GPIO", gpios[i], "ready and raring")

if bestrating[1] > 0:
    GPIO.output(17,True)
    GPIO.output(18,False)
    print("gpio 1 on")
else:
    GPIO.output(18,True)
    GPIO.output(17,False)

next(bestrating)
next(bestrating)
for i in bestrating:
    if bestrating[i] >= 1:
        print("gpios[i+2] on")
        GPIO.output(gpios[i+2],True)
    else:
        print("gpios[1+2] off")
        GPIO.output(gpios[i+2],False)

    
#GPIO.output(17,18,22,23,True
