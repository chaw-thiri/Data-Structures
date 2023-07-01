# T O(n ^ 2)
# S O(n)
def rightSmallerThan(array):

    rightSmallerCounts=[]
    for i in range(len(array)):
        rightSmallerCount=0
        for j in range(i+1,len(array)): # i + 1 = right after the current element
            if array[j]<array[i]:
                rightSmallerCount+=1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts
