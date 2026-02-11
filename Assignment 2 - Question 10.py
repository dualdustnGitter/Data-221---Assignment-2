### Question 10
# make a function that
# 
# prints # of matching lines
# prints first 3 matching lines (in order with number and text)
# 
###

def find_lines_containing(filename, keyword):
    numberOfLinesToShow = 3


    # first check if file exists
    try:
        with open(filename, "r") as textFileInput:
            # print("Ready to go")
            textFileInput.close()
        textFileInput.close()
    except FileNotFoundError:
        print("File Name provided was not valid (found)")
        return "Error"
    

    # open file
    with open(filename, "r") as textFileInput:

        # go through each line
        # checking if keyword is contained
        # if so add line number into a list
        currentTextFileLineNumber = 1
        listOfLineNumbersThatContainKeyword = []
        for singularLineInFile in textFileInput:

            if keyword in singularLineInFile:
                listOfLineNumbersThatContainKeyword.append(currentTextFileLineNumber)

            currentTextFileLineNumber += 1


        # print("Number of lines: " + str(currentTextFileLineNumber))
        # print(listOfLineNumbersThatContainKeyword)


        







find_lines_containing("sample-file.txt", "data")