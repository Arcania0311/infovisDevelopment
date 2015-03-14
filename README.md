# Development of Development

Data processing for our group project in the 2015 Information Visualisation course at the UvA.

## Description

* *Raw.json  
  The raw, uprocessed results of the query. Contains duplicate entries.
* jobIDs.json  
  Contains the details of the queries for all locations. Most important is the job id, so we don't have to run the same query multiple times. Not so important because jobs are not stored that long. T_T
* cleanResults.py  
  Really simple python script that for now only removes duplicate entries, prints the list, and displays a count of the data before cleaning and after.
* processResults.py  
  Again a simple python script, this time to extract data form the cleaned data. Extracts users per city, languages data of a city (commits, users, and commits/user), and activity.  
  * */*Languages.json  
    Contains all languages as keys, with every value another json with keys {commits: x, users: y, commitsPerUser: x/y}.
  * */*Activity.json  
    Contains a list with the activity per weekday, so that [0] is Monday and [6] is Sunday. Every day is a list with 25 entries, so that day[0] is 0-1 o'clock, day[23] is 23-24 o'clock, and day[24] is the total activity of that weekday.
* sample.json  
  Small testing file, rename to test.json to have it covered by gitignore.