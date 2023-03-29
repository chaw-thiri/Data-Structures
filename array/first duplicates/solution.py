# space = O(1), time = O(n^2)
def firstDuplicateValue(array):
    min_inx_of_sec_duplicate = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range( i+1, len(array)):
            value_to_compare = array[j]
            if value == value_to_compare:
                min_inx_of_sec_duplicate = min(min_inx_of_sec_duplicate,j) # replaced by the closest the number to current if, if the original value is larger, it would not be replaced.
    if min_inx_of_sec_duplicate == len(array):
        return -1
    return array[min_inx_of_sec_duplicate]

array =[2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))

