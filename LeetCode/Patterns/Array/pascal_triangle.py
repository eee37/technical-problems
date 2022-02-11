'''
  TIME: O(n**2)
  SPACE: O(n)
'''

from collections import deque

def printPascal(testVariable) :
  if testVariable == 0:
    return [1]
  prev_row = [1]
  row = deque([])
  for level in range(1, testVariable+1):
    for col in range(0, len(prev_row)-1):
      row.append(prev_row[col] + prev_row[col+1])
    row.append(1)
    row.appendleft(1)
    prev_row = row
    if level != testVariable:
      row = deque([]) # NOTE: Need to set to deque
  return list(row) # NOTE: Solution expects list not deque