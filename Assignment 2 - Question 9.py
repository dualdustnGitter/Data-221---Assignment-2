### Question 9
# get tabular data from https://en.wikipedia.org/wiki/Machine_learning
# 
#   get first table in page that has at least 3 data rows
#   get table header with <th> tag if present, otherwise create headers with col1, col2, col3, 
#   if cells are empty fill with ""
#   save extractedd table to wiki_table.csv
###
from bs4 import BeautifulSoup
import requests

# Same thing as the start of question 7 and 8 but with different url
userBrowerserHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/127.0.0.0"} # used opera's user agent thing
rawWebpageFromRequest = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=userBrowerserHeader)
parsedHTMlPageOfWebpage = BeautifulSoup(rawWebpageFromRequest.text, "html5lib")


# get valid th section
allthTagInWebPage = parsedHTMlPageOfWebpage.find_all("table")
stringValidTableToUse = ""

for singularthTable in allthTagInWebPage:
    
    allRowDataInSingularTable = ""

    allRowDataInSingularTable = singularthTable.find_all("tr")

    # try: 
    #     allRowDataInSingularTable = singularthTable.find_all("tr")
    # except UnicodeEncodeError:
    #     print("Unicode Encoding error encountered")
    if len(allRowDataInSingularTable) >= 3:
        stringValidTableToUse = singularthTable
        break

print("Overall Table header:")
print(stringValidTableToUse.find("th").text)
# print(len(stringValidTableToUse.find_all("tr")))


for singularTableRow in stringValidTableToUse.find_all("tr"):
    tableRowHeaderName = ""
    currentTableRowIndex = (stringValidTableToUse.find_all("tr")).index(singularTableRow)
    if singularTableRow.find("th") != None:
        tableRowHeaderName = singularTableRow.find("th").text
    else:
        tableRowHeaderName = "col" + str(currentTableRowIndex)

    # print(tableRowHeaderName)