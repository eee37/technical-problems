'''
******************* PROBLEM STATEMENT
LC # 1604

******************* NOTES
Python Solution is Good
https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/discuss/876864/JavaPython-3-HashMapdict-%2B-Sliding-Window.

NOTES:
    1. Convert time to minutes. Easier to use
    2. Use Sliding window rather than fast and slow pointer
        2.1. Method 2 alternatively uses a queue
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#SlidingWindow #HashMap
'''

'''
    QUESTIONS:
        can a single time entry contribute to multiple alerts
        can assume timestamps are sorted. This is not the case!
    NOTES:
    exp 1
        daniel
        10
        10 40
        11
        luis
        9
        11
        11:30
        13
        15
    exp 2
        alice
            12 01
            12
            18
        bob
            21
            21 20
            21  30
            23
    IDEA # 1
        1. Create map of people to entries
            bob: [8, 9, 10]
        2. For each person use 2 pointers to determine if within the hour. slow and fast pointer. move fast pointer when within the hour of slow pointer. if not let slow catch up to fast until its whithin the hour
            Note:
                once its determined an alert is send can end as list of names in return is unique
        TIME: O(N + NlogN)
'''

from collections import defaultdict
from datetime import datetime
import heapq
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_time = defaultdict(lambda: [])
        
        for keyName, keyTime in zip(keyName, keyTime): # NOTE: Use of zip 
            times = name_time[keyName]
            heapq.heappush(times, keyTime) # NOTE: Assure in sorted order
            
        result = []
        
        for name, times in name_time.items():
            if len(times) < 3:
                continue
            s = 0
            f = 1
            while f < len(times):
                end = datetime.strptime(times[f], '%H:%M')  # NOTE: Time manipulation. strptime converts str to datetime. total_seconds gets difference
                start = datetime.strptime(times[s],'%H:%M') 
                if (abs(end-start)).total_seconds() / 3600 <= 1: # NOTE: Added abs to capture edge case whey key entries fall on different days. I think this is wrong - red herining remove
                    f += 1
                else:
                    s += 1
                if f-s >= 3: # NOTE: Needs to be 3 bc range is [)
                    result.append(name)
                    break
        result.sort() # NOTE: https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/
        return result
                
                
                
            
        