# pass pointers instead of call stacks to reduce space complexity 
# time = O(n ^2 )
# space = O(d) where d is the depth of the array
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0 , 0 , float("-inf"))

def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo,minVal, maxVal):
   
    # both the array are equal
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    # root nodes are equal
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False
    
    # four new roots
    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal) # first left child
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal) 
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne,rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo,rootIdxTwo, maxVal)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo,minVal, currentValue)
    rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame
def getIdxOfFirstSmaller(array, startingIdx, minVal):
    # find the idx of the first smaller value after the starting idx
    # check this value is smaller or equal to the minVal
    # what is the value of the previous parent node in the BST
    # if it isn't then that value is located in the left subtree of the previous parent node
    for i in range(startingIdx+1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal: # minVal is the parent node
            return i 
    return -1


def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    # find the idx of hte first bigger/ equal value after the starting idx
    # make sure that this value is smaller than maxVal, which the 
    # the value of the previous parent node in the Bst
    # if it isn't than the value is located in the right subtree of the previous parent node
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1