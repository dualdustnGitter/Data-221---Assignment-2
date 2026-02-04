### Question 1
# 
# 
# Read textfile
#   split it into words
#   then all to lowercase
#   remove all punctuation from beginning and end
#   only keep words with at least 2 characters
#   
#   then print top 10 most repeated words
### 
punctuationCharacters = ",.!?"

with open("sample-file.txt", "r") as textFileInput:
    # read then convert content to lowercase
    contentsOfFile = textFileInput.read()
    print("--- Original content---\n")
    print(contentsOfFile + "\n\n")

    contentsOfFile = contentsOfFile.lower()
    
    # getting rid of punctuation
    cleaningPunctuationTable = str.maketrans("","",punctuationCharacters) # https://www.w3schools.com/python/ref_string_maketrans.asp 
    newContentsOfFile = contentsOfFile.translate(cleaningPunctuationTable) # in same site ^


    # add the big enough words to a list
    singleTokens = newContentsOfFile.split() # https://www.w3schools.com/python/ref_string_split.asp
    filteredTokens = []
    for singularToken in singleTokens:
        if len(singularToken) >= 2: # the number 2 is the minimum length  aword must have to be kept
            filteredTokens.append(singularToken)
    

    # show the completely filtered contents
    print("--- Filtered content---\n")
    print(" ".join(filteredTokens))



    # now make a dictionary of the (unique) words  
    dictionaryOfUniqueTokensAndQuantities = {}
    for singularToken in filteredTokens:
        if singularToken in list(dictionaryOfUniqueTokensAndQuantities.keys()):
            dictionaryOfUniqueTokensAndQuantities[singularToken] += 1
        else:
             dictionaryOfUniqueTokensAndQuantities[singularToken] = 1

    print("\n\n---Dictionary of unique---\n")

    
    
    # get list of top 10 number of repeated words
    # initialize variables to help show top 10 repeated words with their quantities
    topHowManyNumbersToBeRecorded = 10
    uniqueKeysWithQuantities = ""
    listOfTop10RepeatedTokens = []
    listOfTop10Quantities = []


    # get top 10 largest values
    listOfValuesInDictionary = list(dictionaryOfUniqueTokensAndQuantities.values()) # turn values/quantity of dictionary to a list
    listOfValuesInDictionary = sorted(listOfValuesInDictionary, reverse=True) # have it sort as descended instead
    
    listOfTop10Quantities = listOfValuesInDictionary[:topHowManyNumbersToBeRecorded] # have top 10 recorded only

    # go through top 10 counts
    for quantityOfUniqueKey in listOfTop10Quantities:
        for singularToken in list(dictionaryOfUniqueTokensAndQuantities.keys()): # then get keys with the same value and record them (only if it isnt recorded yet, so doesnt repeat)
            if (singularToken not in listOfTop10RepeatedTokens) and (dictionaryOfUniqueTokensAndQuantities[singularToken] == quantityOfUniqueKey):
                listOfTop10RepeatedTokens.append(singularToken)
                break # exit loop early after finding key with the required value/quantity

        
    # add the top 10 counted words and their quantities and format it into the required format
    for indexCounterForTop10 in range(topHowManyNumbersToBeRecorded):
        uniqueKeysWithQuantities += listOfTop10RepeatedTokens[indexCounterForTop10] + " -> " + str(listOfTop10Quantities[indexCounterForTop10]) + ", "


    print(uniqueKeysWithQuantities)


textFileInput.close()