def getNthFib(n):
    firstTwo =[0,1]
    for num in range(2,n):
        nextNum = firstTwo[0]+firstTwo[1]
        firstTwo[0] = firstTwo[1]
        firstTwo[1] = nextNum
        print(nextNum)
    return firstTwo[1] if n > 1 else firstTwo[0]
# time = O(n), space = O(1)
print(getNthFib(6))