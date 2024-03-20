'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY: nlogn
SPACE COMPLEXITY: n

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''


from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_times = defaultdict(lambda: [])
        for name, time in zip(keyName, keyTime):
            times = name_times[name]
            hr, min = time.split(':') # NOTE: REMEMBER Needs to be converted to int
            day_minutes = 60 * int(hr) + int(min)
            times.append(day_minutes)
        
        response = []

        for name, times in name_times.items():
            if len(times) < 3:
                continue
            times.sort() # NOTE:
            for index in range(2, len(times)):
                if times[index] - times[index - 2] <= 60:
                    response.append(name)
                    break
        response.sort() # NOTE: REMEMBER sorts in place
        return response
                

