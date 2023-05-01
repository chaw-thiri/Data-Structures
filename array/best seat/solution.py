# time = O(n)
# space = O(1)
def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0

    left = 0
    while left < len(seats):
        right = left + 1
        while right< len(seats) and seats[right] == 0: # empty seat
            right += 1

        availableSpace = right- left -1 
        if availableSpace > maxSpace:
            bestSeat = (left + right)//2 # middle seat
            maxSpace = availableSpace
        left = right 
    return bestSeat