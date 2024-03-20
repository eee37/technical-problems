'''
******************* PROBLEM STATEMENT
LC # 937

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#BigO #Array #Sort
'''

'''
    Solution Note:
        Approach 2: Sorting by Keys
            * Uses a single array for sorting. Takes adavantage of the fact that tuple sorting works piece wize
                * Uses first value in tuple to assure alpha go first
                * Finally, thanks to the stability of sorting algorithms, the elements with the same key value would remain the same order as in the original input. 
                Therefore, the Rule (3) is ensured.
                * This assures numeric ones maintain relative order
            * Note that when calculating big O we consider both the number of logs and their size we are using it to compare them
            O(n) of sort = num comparisons at each level log (num of elements)
            Here there are n elements equal to the number of logs. and each comparison requires scanning entire log of an element so number of comparisons at
            each level = M* N where M is maxsize of log. log N is still the size of tree

'''
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_arr = []
        digit_arr = []
        for index, log in enumerate(logs):
            string_arr = log.split()
            type = 'int'
            try: # NOTE: Py Method isalpha(str) Can be used to determine if string is alpha
                int(string_arr[1])
            except ValueError: 
                type = 'string'
            if type == 'int':
                digit_arr.append(logs[index])
            else:
                letter_arr.append(( ' '.join(string_arr[1:]), len(string_arr), string_arr[0], index))
        print(letter_arr)
        letter_arr.sort(key=lambda tup: (tup[0], tup[1], tup[2]) ) # NOTE: Py Method You have to specify the param name. Sort sorts the list in place. Sorted returns a new list
        # NOTE: If two strings are similar but one is larger smaller one goes first
        
        solution = [logs[index]  for a,b,c, index in letter_arr]

        return solution + digit_arr