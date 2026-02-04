### Question 2
# clean content of text file (split into tokens/words, and lowercase it all, remove all punctuations)
# 
#   
# 
# 
# 
### 

with open("sample-file.txt", "r") as textFileInput:
    contentsOfFile = textFileInput.read()

    
    # split into tokens and clean up
    # lowercase contents and split into tokens/words
    listContentsOfFile = (contentsOfFile.lower()).split()
    cleanedUpListOfContents = [] # store list of cleaned words

    # expanded version of punctuation removal
    punctuationCharacters = ",.!?"
    for singularToken in listContentsOfFile:
        if singularToken[0] in punctuationCharacters: # if first character of word is punctuation then remove it

            singularToken = singularToken[1:]
        elif singularToken[len(singularToken)-1] in punctuationCharacters: # if last character of word is punctuation then remove it
            singularToken = singularToken[:len(singularToken)-1]

        # add to cleaned version of list as long as it has a length greater than or equal to 2
        maxWordLengthRequirement = 2 # magic number
        if len(singularToken) >= maxWordLengthRequirement:
            cleanedUpListOfContents.append(singularToken)


    # create lsit of bigrams
    listOfBigrams = []
    for listBigramIndexCounter in range(0, len(cleanedUpListOfContents), 2):
        if listBigramIndexCounter == len(cleanedUpListOfContents)-2: # if its the last word and the length of the cleaned contents is odd then add just the last word 
            listOfBigrams.append(cleanedUpListOfContents[-1:])
        else: # otherwise just add the 2 words as a list into the list of binoms
            listOfBigrams.append(cleanedUpListOfContents[listBigramIndexCounter:listBigramIndexCounter+2])

    
    
    # count amount of repitions of bigrams


textFileInput.close()