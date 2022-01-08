'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#Array
'''

import heapq
def pancake_sort(arr):
  if not arr:
    return []
  
  size = len(arr)
  
  # create max heap
  # heap = [(-el, i) for i, el in enumerate(arr)] # Space of O(n)
  
  # heapq.heapify(heap) # Time O(nlogn) # NOTE: Py. Don't use heapify to sort anything that is not a list. It is not clear what sorting mechanism it uses. Instead use sort or sorted
  
  #heap = sorted(heap, key= lambda tup: tup[0]) # NOTE: This wont work because you will be flipping the array each time

  correct_index = size -1
  for _ in range(0, size):
    #actual_index = heap.pop(0)[1] # NOTE: Need to pop first element
    actual_index = get_max_index(arr, correct_index + 1)
    if correct_index != actual_index:
        # bring largest to 0th index 
        flip(arr, actual_index + 1) # NOTE: Need to convert to non-0 based index
        
        # bring largest to correct index
        flip(arr, correct_index + 1) # NOTE: Need to convert to non-0 based index
    
    correct_index -= 1
  return arr
        
'''
    finds the max's index in arr[:last]
'''
def get_max_index(arr, last):
    max_index = 0
    for index, num in enumerate(arr[:last]):
        if num > arr[max_index]:
            max_index = index
    return max_index



  
def flip(arr, k):
  rev = arr[:k][::-1]
  for i in range(0, k):
    arr[i] = rev[i]
  
arr = [1, 5, 4, 3, 2]


print(pancake_sort([1, 5, 4, 3, 2]))