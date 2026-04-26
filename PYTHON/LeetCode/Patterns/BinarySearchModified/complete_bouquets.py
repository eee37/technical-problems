class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        max_day = max(bloomDay) # search space 1...max_day

        left = 1
        right = max_day

        ans = max_day
        while left<=right:
            mid = left + (right + left) // 2
            # calculate if by midth day is viable and better
            curr = 0
            remaining_bouquets = m
            while curr <= len(bloomDay) - 1: # NOTE: This can be made more efficient. Instead loop over 1...bloomDay and keep track of bouquets and flowers remaining to complete bouquet. Because we are looping over k this solution gives us a slower runtime
                if bloomDay[curr] <= mid:
                    count = 0
                    for i in range(k):
                        if curr + i <= len(bloomDay) - 1 and bloomDay[curr + i] <= mid: # NOTE: Need to make sure within bounds
                            count += 1
                    if count >= k:
                        remaining_bouquets -= 1
                        curr = curr + k
                    else:
                        curr += 1
                else:
                    curr += 1

            if remaining_bouquets <= 0:
                ans = min(ans, mid)
                right = right - 1
            else:
                left = mid + 1
        return ans