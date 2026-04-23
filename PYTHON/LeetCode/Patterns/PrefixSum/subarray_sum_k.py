def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    hashmap = dict()
    hashmap[0] = 1
    prefix_sum = 0
    ans = 0

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in hashmap:
            ans += hashmap[prefix_sum - k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    return ans

        