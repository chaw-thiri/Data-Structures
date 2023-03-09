# a monotonic array is array that  do not show multiple characters: 
# is the arrray is entirely decreasing?? << thinking concept
# isDecreasing = True
# if find non-decresing(increasing or same) 
# (can think entirely opposite too)
# using first two integers, decide the array should go downward or upward.
# if one of the next integers break that trend, that array is monotonic.    
# prompt : empty or single content arrrays are monotonic.
# idea1 : 2 member array can only have one direction.
def isMonotonic(array):
    if len(array) <= 2:
        return 
    direction = array[2]- array[1]
    for i in range(2,len(array)-1):
        difference = array[i]- array[i-1]
        if direction == 0:
            direction = array[i]-array[i-1]
            continue
        if BreakDriection(direction, array[i-1],array[i]):
            return False
    return True
def BreakDriection(direction,previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    elif direction < 0:
        return difference > 0
