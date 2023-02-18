def insertionSort(array):
    for i in range(1,len(array)):   
        h = i
        while h > 0 and array[h-1]> array[h]: # when h < 0 the array would be all sorted
            array[h],array[h-1] = array[h-1],array[h]
            h -= 1
    return array
array = [3,7,5,8,4,2,6,3,9]
print(insertionSort(array))