# s = O(nlog n )
# t = O(n log n )
def mergeSort(array):
    if len(array) == 1:
        return array
    midIdx = len(array) // 2
    leftHalf =array[:midIdx]
    rightHalf = array[midIdx:]
    return mergeSortedArray(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArray(leftHalf, rightHalf):
    sortedArr = [None] * (len(leftHalf)+ len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArr[k] = leftHalf[i]
            i += 1
        else:
            sortedArr[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArr[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArr[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArr
