import json
from datetime import datetime, timedelta

# Set with the predefined top 10 languages
topLangs = {"JavaScript", "Ruby", "Python", "Java", "PHP", "CSS", "Shell", "C++", "C", "Objective-C"}
weekDays = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]
utcOffset = {
  "amsterdam" : 1,
  "bangalore" : 5.5,
  "beijing"   : 8,
  "berlin"    : 1,
  "london"    : 0,
  "madrid"    : 1,
  "moon"      : 0,
  "moscow"    : 3,
  "newYork"   : -5,
  "paris"     : 1,
  "sanFrancisco" : -7,
  "stockholm" : 1,
  "sydney" : 10,
  "tokyo" : 9
}

def convertDate(date):
  result = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
  return result

def newCity():
  city = []
  for i in xrange(24):
    hour = {}
    for lang in topLangs:
      hour[lang] = {}
      for day in weekDays:
        hour[lang][day] = 0

    city.append(hour)

  return city


cityFile = open("totalsPerCity.json")
cityData = json.load(cityFile)
cityFile.close()

finalData = {}

for city in cityData:

  finalData[city] = newCity()

  filepath = "results/" + city + "/" + city + "Clean.json"

  json_data = open(filepath)
  cleanData = json.load(json_data)
  json_data.close()

  for item in cleanData:
    lang = item["repository_language"]

    if lang not in topLangs:
      continue

    dateTime = convertDate(item["created_at"])
    dateTime = dateTime + timedelta(hours=utcOffset[city])
    day = weekDays[dateTime.weekday() - 1]
    
    finalData[city][dateTime.hour][lang][day] += 1

outFinal = "asterPlot/dataTest.json"
with open(outFinal, "w") as outfile:
  json.dump(finalData, outfile)