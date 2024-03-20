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
'''


'''
	SPACE: K Not including ans
	TIME: NlogK

	Finished in Time w. non-optimal solution
    
    TO Improve:
        1. Come up with optimal solution

    General Note:
        Can get away with using squared dist as it does not change order



	NOTE:
		Approach 3 uses binary search. reason we can do this is bc we are not returning in sorted order
			- Essentially we are trying to find k elements.
            NOTE: This solution may not work as well when differences across distances is small.
            In that case better to use squared distances as that will increases differences!

			We have 3 buckets: closest, closer, farther
			closer and farther are re-evaluated at each iteration. closest can only grow

			At each iteration we half the list based on the distance that is halfway between 0 or prev mid and the max value in the list of distances.
			Smaller than this mid-distance are classified as closer and other as farther

			note: low, mid and max are not indices, they represent distances

			Then if length of closer is less than or equal to k. k is updated to be k minus length of closer (k represents reamining elements needed to be found). Remaining is farther and low is mid
			Else remaining is closer and high is mid

			Because k represents remaining elements that need to be found. We do this until its 0

			Potential trip ups:
				while on k != 0

				if len of closer is greater than k
					then split closer in next round
				else 
					add the closer elements to closest and decrease k

				low, mid and high represent distances
				arrays contain indices.

                use squared distance for optimal performance exagerrates difference accross distances

                con worst case of N^2
                con storage is O(N) but this time using twice amount of storage as cacpacity of 3 arrays is N
                distance array is N. Heap solution only required storage of heap
            
        Approach 4 uses quick select
        pro: bc it sorts array in place and doesnt use additional storage reduces space complexity
        to get the O(1) space need to calculate distance on the fly
        questions:
            why do we need to run a check of left at the end?
            in case pivot >= k why is right = pivot - 1
                bc left and and right inclusive [left right]. They reprensent index range where k lies
                and to make this is true we care about the space where k can be and that is [left, pivot -1]
                since pivot after partition is where larger space begins i.e. pivot cannot contain ans

        could add a check to make sure k < size of elements. otherwise can return all elements?
        Potential trip ups:
            There are two ranges the outer one (in quickselect) and the one in partion 
            Outside partition
                left and and right inclusive [left right]. They reprensent index range where k lies
            Inside parition
                [:left) are smaller elements
                [right+1 ...] are larger elements

            bc indexes are 0-based when pivot index == k we are done

            quick select deals with indexes only uses dist for comparisons


            pivot comparison uses <=

            How to select pivot: a + floor((b - a) / 2)

            Once the two pointers meet, we'll need to make sure the left pointer has completely moved past the end of the left side partition, then we can return it back to the QuickSelect function as the pivotIndex representing the left-most edge of the right partition.

            If pivotIndex is equal to k, then we know that the first k values in the array will be the ones we want to select. 
            so [i..k..j] so at the end of each partition i... k-1 are k smallest and k...end are largest

    algo
        pick an element to use as a comparison. its index is the pivot index
        invariant that will be true at the end of each iteration
            [:left) are smaller elements
            (right ...] are larger elements
        while pivot_index is not k
            if pivot index < left do [prev left pivot index) discard larger half
            if pivot index > left [pivot index prev right) discard smaller half
    
'''

import heapq
from typing import List
class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		heap = []

		for index, pt in enumerate(points):
			x,y = pt

			dist = (x**2 + y**2)**.5

			if len(heap) < k:
				heapq.heappush(heap, (-dist, index))
				continue

			if dist < -heap[0][0]: # NOTE: Heap containes tuples
				heapq.heappop(heap)
				heapq.heappush(heap, (-dist, index))
				continue

		return [points[index] for _, index in heap]

