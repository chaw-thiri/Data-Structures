def isPalindrome(string):
    # Write your code here.
    reversedChars=[]
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string=="".join(reversedChars)
