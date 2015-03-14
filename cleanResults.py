# Simple script to remove duplicate entries from the dataset
import sys
import json

def main(argv):
  location = argv[0]
  inputfileName = location + "Raw.json"

  json_data = open(inputfileName)

  rawData = json.load(json_data)
  cleanData = []

  prevCreated = ""
  prevMsg = ""

  for item in rawData:
    if prevCreated == item["created_at"] and prevMsg == item["payload_commit_msg"]:
      continue
    elif prevCreated > item["created_at"]:
      continue
    else:
      cleanData.append(item)
      prevCreated = item["created_at"]
      prevMsg = item["payload_commit_msg"]

  print len(rawData)
  print len(cleanData)

  outputfile = location + "/" + location + "Clean.json"
  with open(outputfile, 'w') as outfile:
    json.dump(cleanData, outfile)

  json_data.close()

if __name__ == "__main__":
  main(sys.argv[1:])