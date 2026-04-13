"""
    #167
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    
    time: O(n)
    space: O(1)
"""
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1

    while numbers[left] + numbers[right] != target and left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
    
    if left < right:
        return [left + 1, right + 1]
    return []

assert twoSum([2,7,11,15],9) == [1,2]
assert twoSum([2,3,4], 6) == [1,3]
assert twoSum([-1,0], -1 ) == [1,2]