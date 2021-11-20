# from collections import default_dict NOTE: COMPILE ERROR
'''
    OFFICIAL SOL OPTIMIZATIONS:
        1) Uses python's hashset set: set(list: list) -> set. item in set -> boolean
        2) max function to update longest consecutive sequence
'''
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = defaultdict(lambda: "NOT FOUND")

        # populate dict
        for num in nums:
            # insert into dict
            key = "NO SEQUENCE"
            # if nums_dict.get(num-1) != "NOT FOUND": NOTE: Silent error
            if nums_dict[num - 1] != "NOT FOUND":
                key = num-1
            nums_dict.update({num: key})

            # update other key
            if nums_dict[num+1] != "NOT FOUND":
                nums_dict.update({num+1: num})

        # find longest sequence
        longest_sequence = 0
        # for num, prev in nums_dict:  NOTE: COMPILE ERROR
        for num, prev in nums_dict.items():
            if prev == "NO SEQUENCE":
                sequence = 1
                next = num + 1
                while nums_dict[next] != "NOT FOUND":
                    next+=1
                    sequence+=1
                if sequence > longest_sequence:
                    longest_sequence = sequence
        return longest_sequence

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))