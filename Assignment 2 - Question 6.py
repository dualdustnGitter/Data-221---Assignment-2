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

#make content of csv file as variable
csvFileInput = pandas.read_csv("crime.csv", delimiter=",")
violentCrimesPerPopColumnOfDataframe = csvFileInput["ViolentCrimesPerPop"]

# make a new column if violent crimes bigger then 0.5 then high crime or else its lowcrime
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



# make 2 groups and average their unemployment rates
for indexOfCSVCounter in range(len(csvFileInput)):
    if listOfRiskValue[indexOfCSVCounter] == "High-Crime":
        listOfHighCrimeUnemployementRate.append(columnOfPctUnemployed[indexOfCSVCounter])
    else:
        listOfLowCrimeUnemployementRate.append(columnOfPctUnemployed[indexOfCSVCounter])

# print avg for both groups (neatly)

print("High crime: \n" + str(numpy.mean(listOfHighCrimeUnemployementRate)))
print("\nLow crime: \n" + str(numpy.mean(listOfLowCrimeUnemployementRate)))