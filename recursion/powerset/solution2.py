# iterative solution 
# time and space = O(n* 2^n)
def powerset(array):
    subsets = [[]]
    for ele in array: 
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets
