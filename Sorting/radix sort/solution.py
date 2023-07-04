# O(d*(n+b)) time
# O(n+b)space : n = length of the input array
def radixSort(array):
    if len(array) == 0:
        return array
    maxNum = max(array)
    digit = 0
    while maxNum / 10 ** digit > 0 : # what is **?\
        countingSort(array,digit)
        digit += 1
    return array

def countingSort(array,digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10
    digitCol = 10 ** digit

    for num in array:
        countIdx = (num // digitCol) % 10
        countArray[countIdx] += 1
    
    for idx in range(1,10):
        countArray[idx] += countArray[idx -1]

    for idx in range(len(array)-1,-1,-1):
        countIdx = (array[idx]//digitCol) % 10
        countArray[countIdx] -= 1
        sortedIdx = countArray[countIdx]
        sortedArray[sortedIdx] = array[idx]

    for idx in range(len(array)):
        array[idx]=sortedArray[idx]
        