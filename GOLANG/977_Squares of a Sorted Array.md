Name the file [leetcode problem id]_[Name of Problem]

# 977 Squares of a Sorted Array
```
Given an integer array nums sorted in increasing order, return an array of the squares of each number sorted in increasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```
### Tags
```
#easy #array
```

### Notes and Takeaways
```
IDEA 1:
    - Using fact that its sorted in increasing order
    - Use two pointers starting at start and end and move to sort squares in decreasing order
    - Return reversal
    This is O(n)
```

### My Solution
```
Time Complexity:
Space Complexity:
``` 