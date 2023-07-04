# time - O(n log n) , S - O(1)
# max heap
def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1,len(array))):
        swap(0, endIdx, array)
        siftDown(0,endIdx-1, array)
    return array
    
def buildMaxHeap( array): 
    
    firstParentIdx = (len(array)-2)//2
    for curIdx in reversed(range(firstParentIdx+1)):
        siftDown(curIdx,len(array)-1, array)

def siftDown(curIdx, endIdx, heap):
    childOneIdx = (2 * curIdx) +1 
    while childOneIdx <= endIdx:
    
        childTwoIdx = (2 * curIdx) + 2 if ( (2 * curIdx) + 2 <= endIdx )else -1 

        if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else: 
            idxToSwap = childOneIdx

        
        # curIdx is parentIdx
        if heap[curIdx] < heap[idxToSwap]:
            swap(curIdx,idxToSwap, heap)
            curIdx = idxToSwap
            childOneIdx = (2 * curIdx) + 1
        else: 
            return 
        
def swap(i,j, array):
    array[i], array[j] = array[j], array[i]
    