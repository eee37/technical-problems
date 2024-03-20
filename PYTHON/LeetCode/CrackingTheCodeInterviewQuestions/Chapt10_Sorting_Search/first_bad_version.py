# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
import math


def isBadVersion(version) -> bool:
    # bad_list = [4, 5]
    bad_list = [3]
    if version in bad_list:
        return True
    else:
        return False


class Solution:
    # @staticmethod
    # def isBadVersion(version) -> bool:
    #     return True
    @staticmethod
    def firstBadVersion(n):
        """
        :type n: int
        :rtype: int
        """
        # NOTE: Need to handle base cases
        if n == 1:
            if isBadVersion(1):
                return 1
            else:
                return None
        return Solution.firstBadVersionRecurse(1, n, n)



    @staticmethod
    def firstBadVersionRecurse(low, high, n):
        if low <= high: # Needs to be <= to handle single element cases
            midpoint = math.floor((high + low) / 2)
            # need to catch case first element is first bad version
            if midpoint == 1 and isBadVersion(1):
                return 1
            if midpoint > 1:
                # Is solution not first case
                if isBadVersion(midpoint) and not isBadVersion(midpoint-1): # NOTE: ! does not exist?
                    return midpoint
                if not isBadVersion(midpoint) and not isBadVersion(midpoint-1):
                    return Solution.firstBadVersionRecurse(midpoint + 1, high, n) # NOTE: Midpoint crossed off so can not include
            if midpoint < n:
                if isBadVersion(midpoint) and isBadVersion(midpoint + 1):
                    return Solution.firstBadVersionRecurse(low, midpoint - 1, n) # NOTE: Midpoint crossed off so can not include
            first_half = Solution.firstBadVersionRecurse(low, midpoint - 1, n)
            second_half = Solution.firstBadVersionRecurse(midpoint + 1, high, n)
            # case where all are bad
            if first_half is None and second_half is None:
                return 1
            if first_half is not None:
                return first_half
            else:
                return second_half
        else:
            return None


if __name__ == '__main__':
    print(Solution.firstBadVersion(3))