### Question 5
# create new column, grand_band
# 
#   low = grade <= 9
#   medium = grade = 10-14
#   high = grade >= 15
### 

import pandas 

# first read the grade column
csvFileInput = pandas.read_csv("student.csv", delimiter=",")
gradeColumnOfCSVDataset = csvFileInput["grade"]

# print(gradeColumnOfCSVDataset)

# list of low med high accoridng to index of grades column
listOfGradeBand = []
for singleGrade in gradeColumnOfCSVDataset:
    if singleGrade >= 15:
        listOfGradeBand.append("High")
    elif singleGrade >= 10:
        listOfGradeBand.append("Medium")
    elif singleGrade >= 0:
        listOfGradeBand.append("Low")


# make new column and palce the values (low med high)
newGrandBandDataframe = pandas.DataFrame(listOfGradeBand)
csvFileInput["grade_band"] = newGrandBandDataframe

# print(csvFileInput)



# create summary table of student bands (number of students, average absences, # of students with itnernet access 1's/total)

numberOfStudents = len(csvFileInput)
# print(numberOfStudents)

absencesColumnOfCSV = csvFileInput["absences"]
# print(absencesColumnOfCSV.mean())

numberOfStudentsWithInternet = (csvFileInput["internet"] == 1).sum()
# print(numberOfStudentsWithInternet)
percentageOfStudentsWithInternet = numberOfStudentsWithInternet/numberOfStudents * 100
# print(percentageOfStudentsWithInternet)


newCSVWithStudentBands = pandas.DataFrame({"Number Of Students": [numberOfStudents],
                                           "Average Of Absences": [absencesColumnOfCSV.mean()],
                                           "Percentage of Students with Internet": [percentageOfStudentsWithInternet]})

# print(newCSVWithStudentBands)

newCSVWithStudentBands.to_csv("student_bands.csv")