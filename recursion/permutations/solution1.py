def getPermutations(array):
    permutations = []
    permutationsHelper(array,[],permutations)
    return permutations
def permutationsHelper(array,currentPermutations,permutations):
    if  len(array) == 0 and len(currentPermutations) != 0: 
        permutations.append(currentPermutations) # return the empty array
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            # print(f"new array :{newArray}")
            # print (f"current permu :{currentPermutations}")


            newPermutation = currentPermutations + [array[i]]
            # print(f"new permutations {newPermutation}")
            # print(permutations)
            # print("\n")
            permutationsHelper(newArray, newPermutation, permutations)
            

array = [1,2,3]
print(getPermutations(array))