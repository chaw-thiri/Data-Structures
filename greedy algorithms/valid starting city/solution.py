# time = O(n) 
# space = O(1)
def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0
    

    for cityIdx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[cityIdx -1]
        fuelFromPreviousCity = fuel[cityIdx -1]
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate
        

       
            
