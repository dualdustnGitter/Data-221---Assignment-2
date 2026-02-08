### Question 4
# load in student.csv
# 
#   filter students, studytime >= 3, itnernet = 1, absences <= 5
#   save filtered data to high_engagement.csv
# 
### 

import pandas

csvFileInput = pandas.read_csv("student.csv", delimiter=",")
# print(csvFileInput)

# create dataframes of column of specified column of original dataframe
gradeColumnOfCSV = csvFileInput["grade"]
studytimeColumnOfCSV = csvFileInput["studytime"]
absencesColumnOfCSV = csvFileInput["absences"]
internetColumnOfCSV = csvFileInput["internet"]

# convert them to lists
listOfGradeColumnOfCSV = gradeColumnOfCSV.to_list()
listOfStudytimeColumnOfCSV = studytimeColumnOfCSV.to_list()
listOfAbsencesColumnOfCSV = absencesColumnOfCSV.to_list()
listOfInternetColumnOfCSV = internetColumnOfCSV.to_list()

# create list of indices of filtered students
listOfFilteredStudentIndices = []


# go through index of all students
# add filtered out students to list
for indexOfStudent in range(len(listOfStudytimeColumnOfCSV)):
    studytimeOfStudent = listOfStudytimeColumnOfCSV[indexOfStudent]
    absencesOfStudent = listOfAbsencesColumnOfCSV[indexOfStudent]
    internetOfStudent = listOfInternetColumnOfCSV[indexOfStudent]


    if studytimeOfStudent >= 3 and absencesOfStudent <= 5 and internetOfStudent == 1:
        listOfFilteredStudentIndices.append(indexOfStudent)

    # print(indexOfStudent)

# print(listOfFilteredStudentIndices)

# change this lsit of filtered student indices to a dataframe
filteredDataframeOfStudents = csvFileInput.loc[listOfFilteredStudentIndices]

# turn it into a csv
filteredDataframeOfStudents.to_csv("high_engagement.csv")