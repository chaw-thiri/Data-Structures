# *** constraint = 0....n , so that u can turn the seen number into negatives
# O(n) time, O(1) space
def firstDuplicateValue(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value -1] < 0:
            return abs_value
        array[abs_value] += -1
    return -1
