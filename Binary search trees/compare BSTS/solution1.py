# time = O(n^2) : n times of O(n)
# space = O(n^2) = no of nodes in each array, due to recursive call stack
# clear ans , suitable for coding interview (45 mins time)

def sameBsts(arrayOne, arrayTwo):
    # len of arrays must be equal
    if len(arrayOne) != len(arrayTwo):
        return False

    # array is empty
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    # root nodes are equal
    if arrayOne[0] != arrayTwo[0]:
        return False

    # left sub trees  
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)

    # right sub trees
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo= getBiggerOrEqual(arrayTwo)


    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmaller(array):
    smaller= []
    for i in range(1, len(array)): # 0 is omitted bc it is root node
        if array[i]< array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerOrEqual(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual 