import json
from datetime import datetime

def convertDate(date):
  result = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
  return result

def newDay():
  day = []
  for i in xrange(24):
    hour = {}
    hour["name"] = str(i)
    hour["commits"] = 0
    day.append(hour)

  return day

# Set with the predefined top 10 languages
topLangs = {"JavaScript", "Ruby", "Python", "Java", "PHP", "CSS", "Shell", "C++", "C", "Objective-C"}
weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

citiesData = {"Mon" : {}, "Tue" : {}, "Wed" : {}, "Thu" : {}, "Fri" : {}, "Sat" : {}, "Sun" : {}}

for days in citiesData:
  citiesData[days]["hours"] = newDay()

location = "moon"
filepath = "results/" + location + "/" + location + "Clean.json"

json_data = open(filepath)
cleanData = json.load(json_data)
json_data.close()

for item in cleanData:
  lang = item["repository_language"]

  if lang not in topLangs:
    continue

  dateTime = convertDate(item["created_at"])
  day = weekDays[dateTime.weekday() - 1]
  
  citiesData[day]["hours"][dateTime.hour]["commits"] += 1

for day in weekDays:
  dailyTotal = 0
  for hour in citiesData[day]["hours"]:
    dailyTotal += hour["commits"]

  citiesData[day]["total"] = {"commits" : round(float(dailyTotal) / 24.0, 2)}

outFinal = "asterPlot/dataTest.json"
with open(outFinal, "w") as outfile:
  json.dump(citiesData, outfile)