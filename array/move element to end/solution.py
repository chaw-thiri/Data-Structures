
def moveElementToEnd(array, toMove):
    start = 0
    end = len(array)-1
    while start < end:
        while start < end and array[end] == toMove:
            end -= 1
        # if array[start] != toMove:  # start += must be done in both conditions, so take it out of the loop
        #     start += 1
        if array[start] == toMove and array[end] != toMove:
            array[start],array[end] = array[end], array[start]
            # start += 1 
        start += 1
    return array
        
