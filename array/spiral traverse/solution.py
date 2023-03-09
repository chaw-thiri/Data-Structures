# SR, SC, ER, EC will be the points where the array changes it direction
# when meet row, jump to next column, when meet column jump next row
# when the outer perimeter is over, move the starting and ending points
# O(n) time, O(n) space, n = the number of items in the array.
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol+1):
            result.append(array[startRow][col])
        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])
        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        for row in reversed(range(startRow+1,endRow)):
            if startCol == endCol:
                break
         # **the second row is startRow + 1 not -
            result.append(array[row][startCol])
        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    return result
