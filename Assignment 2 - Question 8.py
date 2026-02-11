### Quesiton 8
# read from wikipedia
# 
#   get sections from the h2 tag
#   only get ones that dont have a list of statements
#   get rid of any "[edit]" 
### 

from bs4 import BeautifulSoup
import requests


# Same stuff from Question 7
    # Make header so iwkipedia can be accessed
    # access wikipedia
    # parse it into html
userBrowerserHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/127.0.0.0"} # used opera's user agent thing
rawWebpageFromRequest = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=userBrowerserHeader)
parsedHTMlPageOfWebpage = BeautifulSoup(rawWebpageFromRequest.text, "html5lib")

# initialize variables to keep track of valid sections
listOfAllValidh2Sections = []
stringOfAllValidh2Sections = ""
allRawh2SectionsInWebpage = parsedHTMlPageOfWebpage.find_all("h2") # get all sections unfiltered

# banned statements
statementsBannedFromHeader = ["References", "External links", "See also", "or Notes"]

# loop through all statements
for singularh2Section in allRawh2SectionsInWebpage:
    booleanTestForAddingSection = True
    # go through all banned statements then dont add statement if contains 
    for bannedStatement in statementsBannedFromHeader:
        if bannedStatement in singularh2Section:
            # print("Found not valid")
            booleanTestForAddingSection = False

    if booleanTestForAddingSection:
        listOfAllValidh2Sections.append(singularh2Section)
        stringOfAllValidh2Sections += str(stringOfAllValidh2Sections) + str(singularh2Section.text) +"\n"


# create text file then close it
textFileNameToCreate = "headings.txt"
with open(textFileNameToCreate, mode = "w") as textFileToWriteTo:
    textFileToWriteTo.write(stringOfAllValidh2Sections)

textFileToWriteTo.close()