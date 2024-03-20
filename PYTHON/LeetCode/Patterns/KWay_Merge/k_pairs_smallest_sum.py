import heapq
from typing import List

'''
    Solution Explanation:
    https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/209985/python-heap-solution-with-detail-explanation
    NOTE:
    *   This solution is not most optimal as it requires a search on visited array for each tuple encountered
    *   Most optimal Solution: 
        https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
    *   2-Pointer approach does not work here because you may need to backtrack
        e.g.
        Input
        [1,1,2]
        [1,2,3]
        10
        Output
        [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
        Expected
        [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
    *   Tuple Sorting:
        It automatically sorts a list of tuples by the first elements in the tuples, then by the second elements and so on tuple([1,2,3]) will go before tuple([1,2,4]). If you want to override this behaviour pass a callable as the second argument to the sort method.
                             ^
'''


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        visited = []  # used to track what is in heap-queue to prevent duplicates

        while len(result) < k and len(result) < len(nums1) * len(nums2):
            if len(heap) == 0:
                tup = (nums1[0] + nums2[0], 0, 0) # NOTE: that we want to include indexes in tuple since that is what we use to check boundary conditions
                heapq.heappush(heap, tup)
                visited.append(tup)

            next_sum = heapq.heappop(heap)

            result.append([nums1[next_sum[1]], nums2[next_sum[2]]])

            if next_sum[1] + 1 < len(nums1) and (nums1[next_sum[1] + 1] + nums2[next_sum[2]], next_sum[1] + 1, next_sum[2]) not in visited:
                tup = (nums1[next_sum[1] + 1] + nums2[next_sum[2]], next_sum[1] + 1, next_sum[2])
                heapq.heappush(heap, tup)
                visited.append(tup)
            if next_sum[2] + 1 < len(nums2) and (nums1[next_sum[1]] + nums2[next_sum[2] + 1], next_sum[1], next_sum[2] + 1) not in visited:
                tup = (nums1[next_sum[1]] + nums2[next_sum[2] + 1], next_sum[1], next_sum[2] + 1)
                heapq.heappush(heap, tup)
                visited.append(tup)

        return result

    def kSmallestPairsFail(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        left_index = 0
        right_index = 0
        result = []

        while len(result) < k and (
                left_index < len(nums1) - 1 or right_index < len(nums2) - 1):  # NOTE: len -1  bc indexes are 0-indexed
            result.append([nums1[left_index], nums2[right_index]])

            if left_index == len(nums1) - 1:
                right_index += 1
            elif right_index == len(nums2) - 1:
                left_index += 1
            else:
                if nums1[left_index + 1] <= nums2[right_index + 1]:
                    left_index += 1
                else:
                    right_index += 1
        if len(result) < k:
            result.append([nums1[left_index], nums2[right_index]])
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    assert sol.kSmallestPairs([1, 2], [3], 3) == [[1,3],[2,3]]
    assert sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 10) == [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3],
                                                            [1, 3], [2, 3]]
