# Simple script to remove duplicate entries from the dataset
import sys
import json

def main(argv):
  inputfileName = argv[0]

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
      print item

  print len(rawData)
  print len(cleanData)

  json_data.close()

if __name__ == "__main__":
  main(sys.argv[1:])