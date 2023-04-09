# time = O(br)
# space = O(br)
# b = number of blocks , r = number of requirements
def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks,req),reqs)) # ******
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)
    
def getMinDistances(blocks,req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i,closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances
    
def getMaxDistancesAtBlocks(blocks, minDistanceFromBlocks):
    maxDistancesAtBlocks = [0 for _ in blocks]
    for i in range(len(blocks)):
        minDistanceAtBlock = list(map(lambda distances : distances[i], minDistanceFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistanceAtBlock)
    return maxDistancesAtBlocks
    
def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue
    
def distanceBetween(a, b):
    return abs(a - b)