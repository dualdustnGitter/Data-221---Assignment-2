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


    # create list of bigrams
    listOfBigrams = []
    for listBigramIndexCounter in range(0, len(cleanedUpListOfContents), 2):
        if listBigramIndexCounter == len(cleanedUpListOfContents)-2: # if its the last word and the length of the cleaned contents is odd then add just the last word 
            listOfBigrams.append(tuple(cleanedUpListOfContents[-1:])) # convert list (bigram) into tuple so it can be used as a key for dictionary
        else: # otherwise just add the 2 words as a list into the list of binoms
            listOfBigrams.append(tuple(cleanedUpListOfContents[listBigramIndexCounter:listBigramIndexCounter+2])) # same here

    
    # print(listOfBigrams)
    # count amount of repitions of bigrams
    dictionaryOfUniqueBigramsAndQuantities = {}
    for bigramListCounter in range(len(listOfBigrams)):
        if listOfBigrams[bigramListCounter] not in list(dictionaryOfUniqueBigramsAndQuantities.keys()):
            dictionaryOfUniqueBigramsAndQuantities[listOfBigrams[bigramListCounter]] = 1 # if it wasnt counted already count bigram as first appearance
        else:
            dictionaryOfUniqueBigramsAndQuantities[listOfBigrams[bigramListCounter]] += 1 # add onto the count if encountered


    # print(dictionaryOfUniqueBigramsAndQuantities)

    
    # get top 10 repeated bigrams
    topHowManyNumbersToBeRecorded = 10 # to avoid magic numbers
    top10BigramQuantities = sorted(list(dictionaryOfUniqueBigramsAndQuantities.values()), reverse=True) # much like A1 sort by descending (biggest to smallest)
    top10BigramQuantities = top10BigramQuantities[:topHowManyNumbersToBeRecorded] # get first 10 

    top10BigramRepeated = []
    # go through top 10 values 
    for top10BigramQuantityValue in top10BigramQuantities:
        for actualBigram in list(dictionaryOfUniqueBigramsAndQuantities.keys()):
            # again much like A1 find bigrams with same value and not in top 10 list yet, then add it
            if (actualBigram not in top10BigramRepeated) and (dictionaryOfUniqueBigramsAndQuantities[actualBigram] == top10BigramQuantityValue):
                top10BigramRepeated.append(actualBigram)
                break

    # print(top10BigramRepeated)

    # then show the top 10 bigrams and quantities
    for actualBigram in top10BigramRepeated:
        print(str(actualBigram) + " -> " + str(dictionaryOfUniqueBigramsAndQuantities[actualBigram]))

textFileInput.close()