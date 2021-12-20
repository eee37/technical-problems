'''
******************* PROBLEM STATEMENT
LC # 605
#LinkedIn

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: 1

******************* TAGS
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            prev_is_fl = False

            for index, fl in enumerate(flowerbed):
                if not prev_is_fl and fl == 0:
                    if index == len(flowerbed) - 1 or flowerbed[index+1] == 0: # NOTE: Peek at upcoming flowerbed
                        n -= 1
                        prev_is_fl = True
                elif fl == 0:
                    prev_is_fl = False
                elif fl == 1:
                    prev_is_fl = True

                if n <= 0:
                    return True

            return False

