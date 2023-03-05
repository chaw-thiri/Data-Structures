
def isValidSubsequence(array, sequence):
  sequenceIdx = 0 
  for number in array:
    if sequenceIdx == len(sequence):
      return True
    if number == sequence[sequenceIdx]:
      sequenceIdx += 1

  return sequenceIdx == len(sequence)
