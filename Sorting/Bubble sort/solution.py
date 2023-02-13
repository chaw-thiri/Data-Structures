# time = O (n*2) or O (n) | space = O (1)
def bubbleSort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array)-1-counter):
            if array[i+1]<array[i]:
                swap(array, i, i+1)
                sorted = False
    
        counter += 1
    return array
            
def swap(array, i, j):
    array[i],array[j]=array[j],array[i]
array= [8,6,5,3,2,8,9]
print(bubbleSort(array))
