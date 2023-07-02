# T = O(nk) , S = O(n+k)
# n = total num of array elements 
# k = num of arrays
def mergeSortedArrays(arrays):
    sortedList = []
    elementIndexs = [0 for array in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):
            relevantArray = arrays[arrayIdx]
            elementIndex = elementIndexs[arrayIdx]
            if elementIndex == len(relevantArray):
                continue
            smallestItems.append({"arrayIdx":arrayIdx,"num":relevantArray[elementIndex]})
        if len(smallestItems) == 0:
            break
        nextItem = getMinValue(smallestItems)
        sortedList.append(nextItem["num"])
        elementIndexs[nextItem["arrayIdx"]] += 1
    return sortedList
def getMinValue(items):
    minValueIdx = 0
    for i in range(1,len(items)):
        if items[i]["num"] < items[minValueIdx]["num"]:
            minValueIdx = i
    return items[minValueIdx]