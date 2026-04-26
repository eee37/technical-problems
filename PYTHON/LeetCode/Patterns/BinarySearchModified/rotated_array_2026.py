"""
    IDEA 1:
    You can do a linear scan to find the starting point, and then run binary search. That would give you a time complexity of O(n). 
    The best we could possibly do would be O(log n). 
    
    IDEA 2:
    Run binary search, but instead pick a random index. If the element is not found, then return to the first iteration instead of picking the right half of the search space; you picked the left half. You would have to do this at every iteration of binary searching or of slicing, which I believe would give you an O(n) time. 

    IDEA 3 (NOT SOLIDIFIED):
    Run binary search, but we'll take a closer look at the left and right element and determine if it's sorted based on the expected values. 
    1) LEFT <= MID <= RIGHT
    2) LEFT >= MID
    3)

    IDEA 4
    We're running binary search, but we're looking for the pivot element. 
    NOTE: Distinct values
    0[k-1] > O[k], 
    Once we found this pivot element, we can then run binary search on the two halves of the array. 
    Total run time should be O(log n). 
    Note that there's a special case where the size is zero. When the size is zero, we would just want to compare the one single element to the target. 
    What I feel needs to be solidified is how we pick which partition to focus on. 

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)// 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # left partition is sorted
                if nums[left] <= target <= nums[mid]: # in left partition
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right parition is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1


        