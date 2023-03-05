array = [5,4,32,65,3,4,7,8]
sequence = [4,3,7]

def isValidSubsequence(array, sequence):
  arrayIdx = 0
  sequenceIdx = 0 
  while arrayIdx< len(array) and sequenceIdx< len(sequence):
    if array[arrayIdx] == sequence[sequenceIdx]:
      sequenceIdx += 1
    arrayIdx += 1
  return sequenceIdx== len(sequence)

print(isValidSubsequence(array,sequence))