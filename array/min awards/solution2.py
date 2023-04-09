# time = O(n)
# space = O(n)
def minRewards(scores):
    rewards = [ 1 for _ in scores]
    localMinIdxs = getLocakMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdxs(localMinIdx, scores, rewards)
    return sum(rewards)

def getLocakMinIdxs(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i+1]:
            localMinIdxs.append(i)
        if i == len(array)-1 and array[i] < array[i-1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(array)-1:
            continue
        if array[i] < array[i+1] and array[i] < array[i-1]:
            localMinIdxs.append(i)
    return localMinIdxs

def expandFromLocalMinIdxs(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx],rewards[leftIdx+1]+1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx< len(scores) and scores[rightIdx] > scores[rightIdx-1]:
        rewards[rightIdx] = rewards[rightIdx-1]+1
        rightIdx += 1