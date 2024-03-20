import math
from typing import List

# recursive
def binary_search(arr: List, low: int, high: int, target: int) -> int:
    if high >= low: # or equal to bc you need to process single element
        midpoint = math.floor(high - low / 2)
        if arr[midpoint] == target:
            return midpoint
        if target < arr[midpoint]:
            return binary_search(arr, low, midpoint - 1, target) # can exclude midpoint cause was checked
        else:
            return binary_search(arr, midpoint + 1, high, target)
    return None

def binary_search_while(arr: List, target: int) -> int: #TODO: stack overflow issue
    low = 0
    high = len(arr) - 1

    while high >= low:
        med = math.floor((high - low) / 2) + low # NOTE: NEED TO SUM LOW (OFFSET) BC LOW IS NOT AT START
        if arr[med] == target:
            return med
        elif arr[med] < target:
            low = med + 1
        else:
            high = med - 1
    return None



if __name__  == '__main__':
    # assert binary_search([0,1,2,3,4,5], 0, 5, 5) == 5
    # assert binary_search([0], 0, 0, 0) == 0
    # assert binary_search_while([0,1,2,3,4,5], 5) == 5
    print(binary_search([0,1,2,3,4,5], 0, 5, 5))
    assert binary_search_while([0], 0) == 0