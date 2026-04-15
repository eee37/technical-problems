"""
    #238
    Buggy Implementation

"""
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = []
    right = []

    for index, num in enumerate(nums):
        if index-1>0:
            left.append(num * left[index-1])
        else:
            left.append(num)
    print(left)

    right = [1] * len(nums)
    for index in range(len(nums)-1, -1, -1): # I BELIVE RANGE IS [) - does not include right limit
        print(f"index {index}")
        if (index+1) < len(nums):
            right.append(nums[index] * right[index+1])
        else:
            right[index] = nums[index]
    print(right)

    ans = []
    for index in range(len(nums)):
        left_multiple = 1 if index - 1 < 0 else left[index-1]
        right_multiple = 1 if index + 1 > (len(nums) -1) else right[index+1]
        ans.append(left_multiple * right_multiple)
    return ans

nums = [1,2,3,4]
assert productExceptSelf(nums) == [24,12,8,6]