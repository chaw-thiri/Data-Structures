# O(w^2 * h) time 
# O(w) space 
# w = width and h = height of the input array
def waterfallStreams(array, source):
    rowAbove = array[0][:] 
    # [:] = make a shallow copy of the array allowing to modify the copy without damaging the original.
    # -1 = water
    rowAbove[source]= -1

    for row in range(1,len(array)):
        currentRow = array[row][:]
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove == -1 # check -1
            hasBlock = currentRow[idx]== 1 # 1

            if not hasWaterAbove:
                # if there is no water above 
                continue

            if not hasBlock:
                # if there is no block in the current column, move the water below
                currentRow[idx] += valueAbove # the row goes down ...currentRow[idx] << rowAbove[idx]
                continue

            splitWater = valueAbove/2

            # move water right 
            rightIdx = idx
            while rightIdx+1 < len(rowAbove): # condition to prevent going beyond the wall
                rightIdx += 1
                if rowAbove[rightIdx] == 1: # if there is a block in the way
                    break
                if currentRow[rightIdx] != 1: # if there is no water on the right side 
                    currentRow[rightIdx] += splitWater
                    break

            #move water left
            leftIdx = idx
            while leftIdx - 1 >= 0: # condition to prevent going beyond the wall
                leftIdx -= 1
                if rowAbove[leftIdx] == 1: # if there is a block in the way
                    break
                if  currentRow[leftIdx] != 1: # if there is no water below us
                    currentRow[leftIdx] += splitWater
                    break

        rowAbove = currentRow
    
    #covert the decimal to the percnetages of water
    finalPercentages = list(map(lambda num: num *-100, rowAbove))

    return finalPercentages

