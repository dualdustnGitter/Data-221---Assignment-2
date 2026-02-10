### Question 7
# extract sturcture from https://en.wikipedia.org/wiki/Data_science with beautiful soup
# 
#   extracts/prints <title> tag
#   extracts first paragraph (inside div, id: mw-content-text)
#   at least 50 chars without spaces
###

from bs4 import BeautifulSoup
import requests

# this "header" is needed since wikipedia blocks "bots" from accessing their website
# by adding this "header"/user agent it allows the program to access wikipedia
userBrowerserHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/127.0.0.0"} # used opera's user agent thing


rawWebpageFromRequest = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=userBrowerserHeader) # just copied this from lecture, apparently returns a request.Response object then .text converts it to uniCodez
# rawWebpageFromRequest.raise_for_status() # check if grabbing info from wiki page works testing stuff

parsedHTMlPageOfWebpage = BeautifulSoup(rawWebpageFromRequest.text, "html5lib")

titleOfWebpage = parsedHTMlPageOfWebpage.find("title")

listOfAllParagraphsInWebPage = parsedHTMlPageOfWebpage.find_all("p")

validParagraphInWebPage = ""

for paragraphInWebPage in listOfAllParagraphsInWebPage:
    cleanParagraphInWebPage = ((paragraphInWebPage).get_text())
    # print(len(paragraphInWebPage))
    if cleanParagraphInWebPage != None and len(cleanParagraphInWebPage.replace(" ", "")) >= 50:
        # print("found")
        validParagraphInWebPage = cleanParagraphInWebPage
        # print(validParagraphInWebPage)
        break




print("Title of Webpage:")
print(titleOfWebpage.get_text())
print("\nValid paragraph:")
print(validParagraphInWebPage)

# print()
# print(listOfAllParagraphsInWebPage[1].get_text())
# print(len(listOfAllParagraphsInWebPage[1].get_text()))