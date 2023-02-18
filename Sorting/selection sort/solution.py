def selectioSort(array):
    return selectionSortHelper(array,0)
def selectionSortHelper(array,smallestIndex):
    j = smallestIndex  # j is the index of the smallest number in the array. here we assume index 0 as the smallest number.
    while j != len(array):
        for i in range(j,len(array)):
            if array[i]<=array[smallestIndex]:
                smallestIndex= i
                #  
        array[smallestIndex], array[j] = array[j],array[smallestIndex]
        j += 1
        return selectionSortHelper(array,j)
    return array
array= [3,7,3,7,2,4,1,5,6]
print(selectioSort(array))
