<<<<<<< HEAD
def findThreeLargestNumbers(array):
    max_list = []
    for i in range(3):
        max_num = max(array)
        max_list.append(max_num)
        array.remove(max_num)
    final_list = sorted(max_list)
    return final_list
array = input('Type in the array : ').split(',')
array = list(map(int,array))
=======
def findThreeLargestNumbers(array):
    max_list = []
    for i in range(3):
        max_num = max(array)
        max_list.append(max_num)
        array.remove(max_num)
    final_list = sorted(max_list)
    return final_list
array = input('Type in the array : ').split(',')
array = list(map(int,array))
>>>>>>> d78acb4c6da258794be158e5786ea3c7606f7b1e
print(findThreeLargestNumbers(array))