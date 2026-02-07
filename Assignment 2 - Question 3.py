### Question 3
# take in text file
# 
#   each line as a "sentence"
#   cpnvert liens to lowercase and remove whitespace
#   report if they are similar/the same
### 

with open("sample-file.txt", "r") as actualFile:
    # variables to initiate
    lineCounter = 0
    dictionaryOfUniqueLines = {}
    listOfFileLines = []
    listOfCleanFileLines = []

    # go through single lines of text file
    for singleLineOfFile in actualFile:

        # if its not just an empty line
        if singleLineOfFile != "\n":
            # start recording line
            lineCounter += 1
            listOfFileLines.append(singleLineOfFile)

            # clean up line, remove punctuation and spaces
            singleLineOfFile = singleLineOfFile.replace(" ", "").lower()
            singleLineOfFile = singleLineOfFile.replace(",", "")
            singleLineOfFile = singleLineOfFile.replace(".", "")
            singleLineOfFile = singleLineOfFile.replace("?", "")
            singleLineOfFile = singleLineOfFile.replace("!", "")
            singleLineOfFile = singleLineOfFile.replace("-", "")

            # print(str(lineCounter) + " " + (singleLineOfFile))

            # record unique Line's and add to count if its repeated
            listOfCleanFileLines.append(singleLineOfFile)
            if singleLineOfFile not in (dictionaryOfUniqueLines.keys()):
                dictionaryOfUniqueLines[singleLineOfFile] = 1
            else:
                dictionaryOfUniqueLines[singleLineOfFile] += 1

    # sort the highest repeated line quantities to lowest
    top2RepeatedLineQuantities = sorted(list(dictionaryOfUniqueLines.values()), reverse=True)
    top2RepeatedLine = []

    topHowManyNumber = 2 # magic number to pick top 2 lines that are repeated


    # go through top 2 quantities of repeated Lines
    for targetQuantity in top2RepeatedLineQuantities[:topHowManyNumber]:
        # then go through the entire list of unique Lines
        for currentCheckLine in list(dictionaryOfUniqueLines.keys()):
            # if current line is not in list containing top 2 repeated lines and make sure the lines have the same quantitycount as specified in list that keeps track of top 2 quantities
            if currentCheckLine not in top2RepeatedLine and dictionaryOfUniqueLines[currentCheckLine] == targetQuantity:
                # if its found then add it to a list and break out of loop early
                top2RepeatedLine.append(currentCheckLine)
                break



    # loops through top 2 repeated lines
    for targetLine in top2RepeatedLine:
        # print(targetLine)
        # varaibles to keep count of stuff
        listOfTopRepeatedLineIndices = []
        currentLineIndex = 0
        # goes through list of cleaned up lines
        for currentCheckLine in listOfCleanFileLines:
            # if the current Line is the targeted line then add index to a list that keeps track of it
            if currentCheckLine == targetLine:
                listOfTopRepeatedLineIndices.append(currentLineIndex)
            # or else add to the index counter and make sure it doenst go past the len(list)-1 or else out of bounds error
            if currentLineIndex < len(listOfFileLines)-1:
                currentLineIndex += 1

        # go through indices of targeted line then print it
        for currentIndex in listOfTopRepeatedLineIndices:
            print("[" + str(currentIndex) + "]" + " - " + listOfFileLines[currentIndex].replace("\n",""))
        # make a new line then continue
        print()



        # for lineIndex in listOfTopRepeatedLineIndices:
        #     print(str(lineIndex) + " " + listOfFileLines[lineIndex])




actualFile.close()