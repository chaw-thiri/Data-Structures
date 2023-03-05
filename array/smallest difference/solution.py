def smallestDifference(array_one, array_two):
    array_one.sort()  # sort the arrays to simplify the comparison
    array_two.sort()
    
    idx_one = 0  # initialize indices for both arrays
    idx_two = 0
    smallest_diff = float('inf')
    smallest_pair = []

    while idx_one < len(array_one) and idx_two < len(array_two):
        num_one = array_one[idx_one]
        num_two = array_two[idx_two]
        current_diff = abs(num_one - num_two)

        if current_diff < smallest_diff:  # update the smallest difference and pair
            smallest_diff = current_diff
            smallest_pair = [num_one, num_two]

        if num_one < num_two:  # move the index of the array with the smaller number
            idx_one += 1
        else:
            idx_two += 1

    return smallest_pair
# time = O (nlogn + m log m ) where n is the length of first array and m; second array
# space = O(1)