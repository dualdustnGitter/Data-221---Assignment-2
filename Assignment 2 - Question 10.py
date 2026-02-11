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


        # if the number of lines that contain keyword is less then the desired amount then change it to that amount
        if len(listOfLineNumbersThatContainKeyword) < numberOfLinesToShow:
            numberOfLinesToShow = len(listOfLineNumbersThatContainKeyword)



        # print("Number of lines: " + str(currentTextFileLineNumber))
        # print(listOfLineNumbersThatContainKeyword)

        # report # of matching lines
        print("Number of lines containing keyword: " + str(len(listOfLineNumbersThatContainKeyword)))
        print("\nFirst " + str(numberOfLinesToShow) + " line(s) containing \"" + keyword + "\":")


        # report first 3 liens that contain keyword
        for topXnumberOfLinesToShow in range(numberOfLinesToShow):
            lineNumberToShow = listOfLineNumbersThatContainKeyword[topXnumberOfLinesToShow]
            # print("Printing line: " + str(lineNumberToShow))


            textFileInput.seek(0)
            currentTextFileLineNumber = 1
            for singleTextFileLine in textFileInput:
                if currentTextFileLineNumber == lineNumberToShow:
                    print("[" + (str(currentTextFileLineNumber)) + "] " + singleTextFileLine.strip())
                    break

                currentTextFileLineNumber += 1
                






# calling the function
find_lines_containing("sample-file.txt", "lorem")