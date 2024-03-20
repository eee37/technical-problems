'''
  TIME: O(min(N, M))
  SPACE: O(1)
'''

def gcd(testVariable1, testVariable2) :
  # Write your code here
  # Assuming postive numbers
  if testVariable1 == 0 or testVariable2 == 0:
    return 0
  max_sol = 1
  for divisor in range(1, min(testVariable1, testVariable2) + 1): # NOTE: Edge case where testVariable1 == testVariable2 fails w/o + 1
    if (testVariable1 % divisor) == 0 and (testVariable2 % divisor) == 0:
      max_sol = divisor
  return max_sol