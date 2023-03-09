# time = O(n)/ space = O(1)
def isPalindrome(array):
    start = 0
    end = len(array)-1
    if len(array) <= 0: 
        # all the array of len 1 or 0 are palindromes
        return True
    while start < end:
        # print(f"checking start {array[start]} vs end {array[end]}")
        if array[start] == array[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
print(isPalindrome('abcdcba'))