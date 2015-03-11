# Development of Development

Data processing for our group project in the 2015 Information Visualisation course at the UvA.

## Description

* amsterdamRaw.json
  The raw, uprocessed results of the query. Contains duplicate entries.
* jobIDs.json
  Contains the details of the queries for all locations. Most important is the job id, so we don't have to run the same query multiple times.
* cleanResults.py
  Really simple python script that for now only removes duplicate entries, prints the list, and displays a count of the data before cleaning and after.
* test.json
  Sample file for quick testing.