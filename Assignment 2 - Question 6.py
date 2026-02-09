### Question 6
# make variable called ViolentCrimesPerPop
# make simple cato based on crime lvl and compare it to unemployment rates
#   
#   group into high crime and low crime
#   for each group calc avg val of PctUnemployed
#   print avg uneployment rate for both groups
#   
### 

import pandas

csvFileInput = pandas.read_csv("crime.csv", delimiter=",")

violentCrimesPerPopColumnOfDataframe = csvFileInput["ViolentCrimesPerPop"]


listOfRiskValue = []
for numberOfViolentCrimes in violentCrimesPerPopColumnOfDataframe:
    if numberOfViolentCrimes > 0.5:
        listOfRiskValue.append("High-Crime")
    else:
        listOfRiskValue.append("LowCrime")

columnOfViolentCrimes = pandas.DataFrame(listOfRiskValue)


# group it into another csv


# calc ag of pctunemplyed per group

# print avg for both groups (neatly)