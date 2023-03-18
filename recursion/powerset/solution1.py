# recursive solution

def powerset(array,idx = None):
    if idx is None: 
    # first time call the function 
        idx = len(array)-1
    if idx <0: 
    # = x in powerpoint 
        return [[]]
    ele = array[idx]

    subsets = powerset(array, idx - 1)

    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

# [1,2,3,4]
# ele = 4
# subset = powerset([1,2,3])
# add 3 to all subsets in powerset of [1,2,3] done by for block
#####
# [1,2,3]
# ele = 3
# subset = powerset([1,2])
#######
