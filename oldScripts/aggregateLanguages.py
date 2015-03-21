import json

totalFile = open("../totalsPerCity.json")
totalData = json.load(totalFile)
totalFile.close()

totalLanguages = {}

for city in totalData:
  filePath = "../results/" + city + "/" + city + "Languages.json"
  langFile = open(filePath)
  langData = json.load(langFile)
  langFile.close()

  for lang in langData:
    if lang in totalLanguages:
      totalLanguages[lang]["users"] += langData[lang]["users"]
      totalLanguages[lang]["commits"] += langData[lang]["commits"]
    else:
      totalLanguages[lang] = {}
      totalLanguages[lang]["users"] = langData[lang]["users"]
      totalLanguages[lang]["commits"] = langData[lang]["commits"]

for lang in totalLanguages:
  totalLanguages[lang]["commitsPerUser"] = round(float(totalLanguages[lang]["commits"]) / round(totalLanguages[lang]["users"]), 2)

outLanguages = "../totalsPerLanguage.json"
with open(outLanguages, "w") as outfile:
  json.dump(totalLanguages, outfile)
  print "Finished languages."