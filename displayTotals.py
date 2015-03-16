import json

totalFile = open("totalsPerCity.json")
data = json.load(totalFile)
totalFile.close()

for city in data:
  print city + " : " + str(data[city])