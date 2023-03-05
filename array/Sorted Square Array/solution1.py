# time = O(nlogn) 
# used sort function, not optimal solution
# space = O(n)
# new array = new data structure thus O(n)
def sortedSquaredArray(array):
  final_array= []
  for i in range(len(array)):
      final_array.append(array[i]**2)
  return sorted(final_array)
print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))