# Simple script to process the data
import sys
import json
from datetime import datetime

def convertDate(date):
  result = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
  return result

def main(argv):
  location = argv[0]
  filepath = "results/" + location + "/" + location
  inputfileName =  filepath + "Clean.json"

  json_data = open(inputfileName)
  rawData = json.load(json_data)
  json_data.close()

  users = {}
  languages = {}

  # Create empty activity hours list
  activity = [[],[],[],[],[],[],[]]
  for day in activity:
    for i in xrange(24):
      day.append(0)

  # Commits per language per user & acivity through the day
  print "Processing users and activity..."
  for item in rawData:
    dateTime = convertDate(item["created_at"])
    activity[dateTime.weekday()][dateTime.hour] += 1

    if item["actor_attributes_login"] in users:
      if item["repository_language"] in users[item["actor_attributes_login"]]:
        users[item["actor_attributes_login"]][item["repository_language"]] += 1
      else:
        users[item["actor_attributes_login"]][item["repository_language"]] = 1
    else:
      users[item["actor_attributes_login"]] = {}
      users[item["actor_attributes_login"]][item["repository_language"]] = 1

  # Total activity per day
  for day in activity:
    total = 0
    for hour in day:
      total += hour
    day.append(total)

  # Append activity per day/hour to json
  outActivity = filepath + "Activity.json"
  with open(outActivity, "w") as outfile:
    json.dump(activity, outfile)
    print "Finished activity."


  # Append users per city to json
  with open("totalsPerCity.json", 'r') as infile:
    outTotals = json.load(infile)
    totalCommits = len(rawData)
    totalUsers = len(users)
    totalCpU = round(float(totalCommits) / float(totalUsers), 2)
    outTotals.update({location : {"commits" : totalCommits, "users" : totalUsers, "commitsPerUser" : totalCpU}})

  with open("totalsPerCity.json", 'w') as outfile:
    json.dump(outTotals, outfile)
    print "Finished totals."


  # Users per language
  print "Processing language data."
  for item in users:
    for lang in users[item]:
      if lang in languages:
        languages[lang]["users"] += 1
        languages[lang]["commits"] += users[item][lang]
      else:
        languages[lang] = {}
        languages[lang]["users"] = 1
        languages[lang]["commits"] = users[item][lang]

  for lang in languages:
    languages[lang]["commitsPerUser"] = round(float(languages[lang]["commits"]) / float(languages[lang]["users"]), 2)

  outLanguages = filepath + "Languages.json"
  with open(outLanguages, "w") as outfile:
    json.dump(languages, outfile)
    print "Finished languages."

if __name__ == "__main__":
  main(sys.argv[1:])