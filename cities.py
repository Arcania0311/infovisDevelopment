import json
from difflib import SequenceMatcher 

cityFile = open("citiesRaw.json")
cityData = json.load(cityFile)
cityFile.close()

cities = []

for city in cityData:
  cities.append(city['actor_attributes_location'])

finalData = {}
simCities = []

for city in cities:
  print "\nExisting groups."
  for i, val in enumerate(simCities):
    print str(i) + ", " + val

  print city
  x = input("-1 for new. -2 to discard.\n")
  
  if x == -2:
    continue
  elif x == -1:
    finalData[city] = []
    simCities.append(city)
  elif x == 100:
    break
  else:
    finalData[simCities[x]].append(city)

outputfile = "simCities.json"
with open(outputfile, 'w') as outfile:
  json.dump(finalData, outfile)