### Question 4
# load in student.csv
# 
#   filter students, studytime >= 3, itnernet = 1, absences <= 5
#   save filtered data to high_engagement.csv
# 
### 

import pandas

csvFileInput = pandas.read_csv("student.csv", delimiter=",")
print(csvFileInput)

studytimeColumnOfCSV = csvFileInput["grade"]
absencesColumnOfCSV = csvFileInput["absences"]
internetColumnOfCSV = csvFileInput["internet"]

