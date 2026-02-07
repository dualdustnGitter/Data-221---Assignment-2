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


    for targetQuantity in top2RepeatedLineQuantities[:topHowManyNumber]:
        for currentCheckLine in list(dictionaryOfUniqueLines.keys()):
            if currentCheckLine not in top2RepeatedLine and dictionaryOfUniqueLines[currentCheckLine] == targetQuantity:
                top2RepeatedLine.append(currentCheckLine)
                break



    for targetLine in top2RepeatedLine:
        # print(targetLine)
        listOfTopRepeatedLineIndices = []
        currentLineIndex = 0
        for currentCheckLine in listOfCleanFileLines:
            if currentCheckLine == targetLine:
                listOfTopRepeatedLineIndices.append(currentLineIndex)
            if currentLineIndex < len(listOfFileLines)-1:
                currentLineIndex += 1

        for currentIndex in listOfTopRepeatedLineIndices:
            print("[" + str(currentIndex) + "]" + " - " + listOfFileLines[currentIndex].replace("\n",""))
        print()



        # for lineIndex in listOfTopRepeatedLineIndices:
        #     print(str(lineIndex) + " " + listOfFileLines[lineIndex])














actualFile.close()