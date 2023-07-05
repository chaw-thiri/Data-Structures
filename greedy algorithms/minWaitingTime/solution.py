# T = O(n log n), due to sorting 
# S = O(1)
def minimumWaitingTime(queries):
    queries.sort() # t = n log n 

    totalWaitingTime = 0

    for idx, duration in enumerate(queries): # n
        queriesleft = len(queries)-(idx+1)   # idx = +1 cuz idx starts at 0
        totalWaitingTime += duration * queriesleft

    return totalWaitingTime


# since n log n > n , net = O(n log n)