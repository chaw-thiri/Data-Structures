# time = O(n) : go through the array only one time
# space = O(n) : create new array
def sortedSquaredArray(array):
  start = 0
  end = len(array)-1
  new_array=[]
  while start<=end:
    if abs(array[start]) > abs(array[end]):
      new_array.insert(0,(array[start])**2)
      start += 1
    else:
      new_array.insert(0,(array[end])**2)
      end -= 1
  return new_array
print(sortedSquaredArray([1, -2, 3, -5, 6, 8, 9]))