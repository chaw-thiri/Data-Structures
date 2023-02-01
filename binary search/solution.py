# python 
# binary_search : search the target number using binary search method.
def binary_search(array,target):
    if target not in array:
        return -1
    else:
        sorted_array = sorted(array)
        while True:
            mid_point= round(len(sorted_array)/2)
            small_half = sorted_array[:mid_point]
            big_half = sorted_array[mid_point:]
            big_first_number = big_half[0]
            if big_first_number == target:
                return array.index(big_first_number)
            elif target > big_first_number:
                sorted_array = big_half
            elif target < big_first_number:
                sorted_array = small_half
user_string = input("Type your list of number : ")
user_list = user_string.split(',')
user_list = list(map(float,user_list))
user_number = float(input('Type the number u are finding?'))
print(binary_search(user_list, user_number))