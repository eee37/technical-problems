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

# TODO: Return to debug

from typing import List


class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		if len(points) < k:
			return points

		left = 0
		right = len(points) - 1

		# pivot = self.partition(left, right, self.get_pivot(left, right)) 
		# NOTE: don't want to do this yet. Because then you also need to update left, right here => repetetive

		pivot = None # 

		while k != pivot:
			pivot = self.partition(left, right, self.get_pivot(left, right))

			if k < pivot: # NOTE: Equal case handled differently. Is that okay?
				right = pivot - 1
			else:
				left = pivot

		return points[:pivot] # NOTE:


	# returns pivot
	def partition(self, l:int, r: int, pivot: int, points: List[List[int]]) -> int:
		pivot_dist = self.get_dist(points[pivot]) # NOTE: get dist expects list. IMPORTANT: Remember what get_dist and get_pivot expect and return

		while r >= l: # until they cross. NOTE: Different; what about when l=r? Is that okay?
			if self.get_dist(points[l]) <= pivot_dist: # NOTE: get_dist expects List/point not index. Equal case handled differently. Is that okay?
				l += 1
			else:
				points[l], points[r] =  points[r], points[l] # swap
				right -= 1
		return l






	def get_pivot(self, left: int, right: int) -> int:
		return left + ((right  - left ) // 2) # NOTE: Remember in this case it resurns pivot

	def get_dist(self, point: int) -> int:
		return point[0]**2 + point[1]**2