# python
# search in sorted matrix
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target = 44


def searchInSortedMatrix(matrix, target):
    row = len(matrix) - 1
    column = 0
    while row >= 0 and column <= len(matrix[0]):
        if matrix[row][column] > target:
            row -= 1
        elif matrix[row][column] < target:
            column += 1
        elif matrix[row][column] == target:
            return [row,column]
    return [-1,-1]
print(searchInSortedMatrix(matrix,target))
