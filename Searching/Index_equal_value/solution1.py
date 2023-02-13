 # time = O (n) space = O (1)

def indexEqualsValue(array):
    for i in range(len(array)):
        value = array[i]
        if i == value:
            return i 
    return -1 
array = [-5, -3, 0, 3, 4, 5, 9]
print(indexEqualsValue(array))

