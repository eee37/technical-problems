'''
******************* PROBLEM STATEMENT
https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnpZ

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#hashmap
'''

'''
Note distinct elements aren't actually allowed
'''
from collections import defaultdict
def find_pairs_with_given_difference(arr, k):
  hashmap = defaultdict(lambda: None)
  counter = defaultdict(lambda: 0)
  for num in arr:
    counter[num] = counter[num] + 1
    x = k + num
    hashmap.update({num: x})
   
  result = []
  for num in arr:
    x = hashmap[num]
    if x not in counter or ( k==0 and counter[x] <= 1 ):
      continue
    result.append([x, num])
  
  return result     
  

print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 0))
print(find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))