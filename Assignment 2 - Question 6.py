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
import numpy

csvFileInput = pandas.read_csv("crime.csv", delimiter=",")

violentCrimesPerPopColumnOfDataframe = csvFileInput["ViolentCrimesPerPop"]


listOfRiskValue = []
for numberOfViolentCrimes in violentCrimesPerPopColumnOfDataframe:
    if numberOfViolentCrimes > 0.5:
        listOfRiskValue.append("High-Crime")
    else:
        listOfRiskValue.append("LowCrime")

columnOfViolentCrimes = pandas.DataFrame(listOfRiskValue)


# calc ag of pctunemplyed per group
columnOfPctUnemployed = csvFileInput["PctUnemployed"]

listOfHighCrimeUnemployementRate = []
listOfLowCrimeUnemployementRate = []




for indexOfCSVCounter in range(len(csvFileInput)):
    if listOfRiskValue[indexOfCSVCounter] == "High-Crime":
        listOfHighCrimeUnemployementRate.append(columnOfPctUnemployed[indexOfCSVCounter])
    else:
        listOfLowCrimeUnemployementRate.append(columnOfPctUnemployed[indexOfCSVCounter])

# print avg for both groups (neatly)

print("High crime: \n" + str(numpy.mean(listOfHighCrimeUnemployementRate)))
print("\nLow crime: \n" + str(numpy.mean(listOfLowCrimeUnemployementRate)))