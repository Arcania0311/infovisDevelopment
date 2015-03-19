# Development of Development

Data processing for our group project in the 2015 Information Visualisation course at the UvA.

## Description

* aggregateLanguages.py  
  Simple script to quickly aggregate total language data from the seperate city files into a single file.
* cleanResults.py  
  Really simple python script that for now only removes duplicate entries, prints the list, and displays a count of the data before cleaning and after.
* processResults.py  
  Again a simple python script, this time to extract data form the cleaned data. Extracts users per city, languages data of a city (commits, users, and commits/user), and activity.  
  * */*Languages.json  
    Contains all languages as keys, with every value another json with keys {commits: x, users: y, commitsPerUser: x/y}.
  * */*Activity.json  
    Contains a list with the activity per weekday, so that [0] is Monday and [6] is Sunday. Every day is a list with 25 entries, so that day[0] is 0-1 o'clock, day[23] is 23-24 o'clock, and day[24] is the total activity of that weekday.
* radar.py  
  Script to transform the data for diplay in the radar graph, and in the future also the other elements of the visualisation, such as the bar charts.
* tod3.py  
  Script to transform total datafiles into a d3 force graph friendly format.
* sample.json  
  Small testing file, rename to test.json to have it covered by gitignore.