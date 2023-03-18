# O(n) = where n is the number of elements in array including subarray
# O(d) = level of arrays
def productSum(array, multiplier = 1):
    sum = 0
    for elementORlist in array:
        if type(elementORlist) is list:
            sum += productSum(elementORlist, multiplier + 1)
        else:
            sum += elementORlist
    return sum*multiplier
print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))