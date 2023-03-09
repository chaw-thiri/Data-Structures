def longestPeak(arr):
    n = 0
    for num in range(1,len(arr)-1): # the last and first num cannot form a peak
        if arr[num-1]< arr[num] and arr[num+1] < arr[num]: # arr[num] is the peak now 
            leftIdx = RightIdx = num
            while leftIdx > 0 and arr[leftIdx]> arr[leftIdx-1]:
                leftIdx -= 1
            while RightIdx+1 < len(arr) and arr[RightIdx] > arr[RightIdx+1]:
                RightIdx += 1
            n = max(n, (RightIdx-leftIdx+1))
    return n