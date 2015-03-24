import json

finalData = {}

finalData["cities"] = []
finalData["languages"] = []

# Temporary dict to store languages to reduce loops
langDict = {}

langFile = open("../totalsPerLanguage.json")
langData = json.load(langFile)
langFile.close()

cityFile = open("../totalsPerCity.json")
cityData = json.load(cityFile)
cityFile.close()

for city in cityData:
  tempCity = {}
  tempCity["name"] = city
  tempCity["users"] = cityData[city]["users"]
  tempCity["commits"] = cityData[city]["commits"]
  tempCity["commitsPerUser"] = cityData[city]["commitsPerUser"]
  tempCity["langs"] = []

  cityLangFilePath = "../results/" + city + "/" + city + "Languages.json"
  cityLangFile = open(cityLangFilePath)
  cityLangData = json.load(cityLangFile)
  cityLangFile.close()

  for lang in cityLangData:
    tempCityLang = {}
    tempCityLang["name"] = lang
    tempCityLang["users"] = cityLangData[lang]["users"]
    tempCityLang["commits"] = cityLangData[lang]["commits"]
    tempCityLang["commitsPerUser"] = cityLangData[lang]["commitsPerUser"]

    tempCity["langs"].append(tempCityLang)

    if lang in langDict:
      pass
    else:
      langDict[lang] = {}
      
    langDict[lang][city] = {}
    langDict[lang][city]["users"] = cityLangData[lang]["users"]
    langDict[lang][city]["commits"] = cityLangData[lang]["commits"]
    langDict[lang][city]["commitsPerUser"] = cityLangData[lang]["commitsPerUser"]

  for lang in langData:
    found = False
    for cityLang in tempCity["langs"]:
      if cityLang["name"] == lang:
        found = True

    if not found:
      tempCityLang = {}
      tempCityLang["name"] = lang
      tempCityLang["users"] = 0
      tempCityLang["commits"] = 0
      tempCityLang["commitsPerUser"] = 0

      tempCity["langs"].append(tempCityLang)

  finalData["cities"].append(tempCity)

for lang in langDict:
  tempLang = {}
  tempLang["name"] = lang
  tempLang["users"] = langData[lang]["users"]
  tempLang["commits"] = langData[lang]["commits"]
  tempLang["commitsPerUser"] = langData[lang]["commitsPerUser"]
  tempLang["cities"] = []

  for city in langDict[lang]:
    tempLangCity = {}
    tempLangCity["name"] = city
    tempLangCity["users"] = langDict[lang][city]["users"]
    tempLangCity["commits"] = langDict[lang][city]["commits"]
    tempLangCity["commitsPerUser"] = langDict[lang][city]["commitsPerUser"]

    tempLang["cities"].append(tempLangCity)

  for city in cityData:
    found = False
    for langCity in tempLang["cities"]:
      if city == langCity["name"]:
        found = True

    if not found:
      tempLangCity = {}
      tempLangCity["name"] = city
      tempLangCity["users"] = 0
      tempLangCity["commits"] = 0
      tempLangCity["commitsPerUser"] = 0

      tempLang["cities"].append(tempLangCity)    

  finalData["languages"].append(tempLang)

i = 0
for city in finalData["cities"]:
  city["ID"] = i
  i += 1

i = 0
for lang in finalData["languages"]:
  lang["ID"] = i
  i += 1

outFinal = "../dataRadar.json"
with open(outFinal, "w") as outfile:
  json.dump(finalData, outfile)
