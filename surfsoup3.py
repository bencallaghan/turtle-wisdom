import time
import magicseaweed
import pandas as pd

api_key = "54581012c82ad9250600ea521bf8dd24" 
clam_id = 4709
#martinique_id = 371

clam_forecast = magicseaweed.MSW_Forecast(api_key, clam_id)
#clam_now = clam_forecast.get_current()
#print(clam_now.attrs)

clam_future = clam_forecast.get_future()
print(clam_future.summary)

data = pd.DataFrame([])

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

gpios = [17,18,22,23,24]

for i in gpios:
    gpio.setup(gpio[i], out)

if bestrating[1] > 0:
    gpio[1].on()
    print("gpio 1 on")
else:
    print("gpio[2].on()")

for i in 2:length(bestrating):
    if bestrating[i] >= 1:
        print("gpios[i+2] on")
    else:
        print("gpios[1+2] off")


    
