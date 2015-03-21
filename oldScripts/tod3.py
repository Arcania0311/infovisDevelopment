import json

finalData = {}

finalData["nodes"] = []
finalData["links"] = []

IDs = {}

langFile = open("../totalsPerLanguage.json")
langData = json.load(langFile)
langFile.close()

cityFile = open("../totalsPerCity.json")
cityData = json.load(cityFile)
cityFile.close()

newID = 0

# Create nodes
for city in cityData:
  tempCity = {}
  tempCity["ID"] = newID
  tempCity["name"] = city
  tempCity["type"] = "city"
  tempCity["commits"] = cityData[city]["commits"]
  tempCity["users"] = cityData[city]["users"]
  tempCity["commitsPerUser"] = cityData[city]["commitsPerUser"]

  IDs[city] = newID
  newID += 1

  finalData["nodes"].append(tempCity)

for lang in langData:
  tempLang = {}

  tempLang["ID"] = newID
  tempLang["name"] = lang
  tempLang["type"] = "lang"
  tempLang["commits"] = langData[lang]["commits"]
  tempLang["users"] = langData[lang]["users"]
  tempLang["commitsPerUser"] = langData[lang]["commitsPerUser"]

  IDs[lang] = newID
  newID += 1

  finalData["nodes"].append(tempLang)

# Create links
for city in cityData:
  cityLangFilePath = "../results/" + city + "/" + city + "Languages.json"
  cityLangFile = open(cityLangFilePath)
  cityLangData = json.load(cityLangFile)
  cityLangFile.close()

  for lang in cityLangData:
    tempLink = {}

    tempLink["source"] = IDs[city]
    tempLink["target"] = IDs[lang]
    tempLink["commits"] = cityLangData[lang]["commits"]
    tempLink["users"] = cityLangData[lang]["users"]
    tempLink["commitsPerUser"] = cityLangData[lang]["commitsPerUser"]

    finalData["links"].append(tempLink)

outFinal = "../data.json"
with open(outFinal, "w") as outfile:
  json.dump(finalData, outfile)
  print "Finished all the things."

