# s = O(nlog n )
# t = O(n )
def mergeSort(array):
  if len(array) <= 1:
    return array
  auxiArray = array[:]
  mergeSortHelper(array, 0, len(array)-1, auxiArray)
  return array

def mergeSortHelper(mainArr, startIdx, endIdx, auxiArr):
  if startIdx == endIdx: return
  midIdx = (startIdx + endIdx ) //2
  mergeSortHelper(auxiArr, startIdx, midIdx, mainArr)
  mergeSortHelper(auxiArr, midIdx+1, endIdx, mainArr)
  doMerge(mainArr,startIdx,midIdx, endIdx, auxiArr)

def doMerge(mainArr, startIdx, midIdx, endIdx, auxiArr):
  i = startIdx
  k = startIdx
  j = midIdx + 1
  while i <= midIdx and j <= endIdx:

    if auxiArr[i] <= auxiArr[j]:
      mainArr[k] = auxiArr[i]
      i += 1
    else:
      mainArr[k] = auxiArr[j]
      j += 1
    k += 1
  while i <= midIdx:
    mainArr[k] = auxiArr[i]
    i += 1
    k += 1
  while j <= endIdx:
    mainArr[k] = auxiArr[j]
    j += 1
    k += 1
    