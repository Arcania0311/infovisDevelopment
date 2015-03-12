# Simple script to process the data
import sys
import json

def main(argv):
  location = argv[0]
  inputfileName = location + "Clean.json"

  json_data = open(inputfileName)

  rawData = json.load(json_data)
  users = {}
  languages = {}


  for item in rawData:
    print item


  # outputfile = location + "Clean.json"
  # with open(outputfile, 'w') as outfile:
  #   json.dump(cleanData, outfile)

  json_data.close()

if __name__ == "__main__":
  main(sys.argv[1:])