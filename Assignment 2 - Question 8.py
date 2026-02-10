### Quesiton 8
# 
# 
# 
# 
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


listOfAllValidh2Sections = []
stringOfAllValidh2Sections = ""
allRawh2SectionsInWebpage = parsedHTMlPageOfWebpage.find_all("h2")

statementsBannedFromHeader = ["References", "External links", "See also", "or Notes"]
for singularh2Section in allRawh2SectionsInWebpage:
    booleanTestForAddingSection = True
    for bannedStatement in statementsBannedFromHeader:
        if bannedStatement in singularh2Section:
            print("Found not valid")
            booleanTestForAddingSection = False

    if booleanTestForAddingSection:
        listOfAllValidh2Sections.append(singularh2Section)
        stringOfAllValidh2Sections += str(stringOfAllValidh2Sections) + str(singularh2Section) +"\n"




with open("Question 8 Text File.txt", mode = "w") as textFileToWriteTo:
    textFileToWriteTo.write(stringOfAllValidh2Sections)