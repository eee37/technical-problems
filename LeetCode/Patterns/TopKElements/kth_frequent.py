'''
******************* PROBLEM STATEMENT

******************* NOTES
REVIEW:
    DICT: values(), items(), update()
    sorted vs sort, reverse

TIME COMPLEXITY: O(nlogk)
SPACE COMPLEXITY: O(n) Note solution says O(n+k) but doesn't k have to be smaller than n

NOTE:
    1) Base case, when k >= N wouldnt you just return N
    2) Python build-in fxn Counter( dict ) builds frequency dictionary # from collections import Counter
    3) In Approach #1: return heapq.nlargest(k, count.keys(), key=count.get)  means when evaluating size count.get is called on each item of count.keys()
    but top k elements of count.keys are returned based on that evaluation

******************* SOLUTION
'''


from typing import List
import heapq

class Solution:
    # Sorting freq approach
    def topKFrequentSort(self, nums: List[int], k: int) -> List[int]:
        # STEP_1: Create frequency map
        freq = dict()
        for num in nums:
            curr = freq.get(num) # Is there a has key function?
            if not curr:
                freq.update({num: 1}) # NOTE: Update expects dictionary containing new keys
            else:
                freq.update({num: curr + 1})

        # STEP_2: Find Kth most frequent
        topk = sorted(list(freq.values()), reverse=True) # NOTE: Values returns a View object not list (view objects are updated when dict is updated). Sort is methode of list. Sorted is not. Set reverse to True to sort in descending order
        kth = topk[k-1]

        # STEP_3: Create Result
        result = []

        for key, value in freq.items(): # NOTE: Use items to iterate over dict
            if value >= kth: # Use > remember k is the min freq to be in top k
                result.append(key)
            if len(result) == k:
                return result

    # Heap approach
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            curr = freq.get(num)
            if not curr:
                freq.update({num: 1})
            else:
                freq.update({num: curr + 1})

            # STEP_2: Find Kth most frequent
        heap = []
        for f in list(freq.values()):
            if len(heap) < k:
                heapq.heappush(heap, f)
            elif heap[0] < f:
                heapq.heappop(heap)
                heapq.heappush(heap, f)

        kth = heap[0]

        # STEP_3: Create Result
        result = []

        for key, value in freq.items():
            if value >= kth:
                result.append(key)
            if len(result) == k:
                return result

if __name__ == '__main__':
    sol =  Solution()
    assert sol.topKFrequent([1,1,1,2,2,3], 2) == [1,2]