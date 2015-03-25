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

cityFile = open("totalsPerCity.json")
cityData = json.load(cityFile)
cityFile.close()

finalData = {}

for city in cityData:

  citiesData = {"Mon" : {}, "Tue" : {}, "Wed" : {}, "Thu" : {}, "Fri" : {}, "Sat" : {}, "Sun" : {}}

  for days in citiesData:
    for lang in topLangs:
      citiesData[days][lang] = {}
      citiesData[days][lang]["name"] = lang
      citiesData[days][lang]["hours"] = newDay()

  filepath = "results/" + city + "/" + city + "Clean.json"

  json_data = open(filepath)
  cleanData = json.load(json_data)
  json_data.close()

  for item in cleanData:
    lang = item["repository_language"]

    if lang not in topLangs:
      continue

    dateTime = convertDate(item["created_at"])
    day = weekDays[dateTime.weekday() - 1]
    
    citiesData[day][lang]["hours"][dateTime.hour]["commits"] += 1

  for day in weekDays:
    dailyTotal = 0
    for lang in topLangs:
      for hour in citiesData[day][lang]["hours"]:
        dailyTotal += hour["commits"]

      citiesData[day][lang]["total"] = round(float(dailyTotal) / 24.0, 2)

  finalData[city] = citiesData

outFinal = "asterPlot/dataTest.json"
with open(outFinal, "w") as outfile:
  json.dump(finalData, outfile)