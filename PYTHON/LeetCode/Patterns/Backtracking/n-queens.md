ref: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/
```
def backtrack_nqueen(row = 0, count = 0):
    for col in range(n):
        # iterate through columns at the curent row.
        if is_not_under_attack(row, col):
            # explore this partial candidate solution, and mark the attacking zone
            place_queen(row, col)
            if row + 1 == n:
                # we reach the bottom, i.e. we find a solution!
                count += 1
            else:
                # we move on to the next row
                count = backtrack_nqueen(row + 1, count)
            # backtrack, i.e. remove the queen and remove the attacking zone.
            # remove queen to explore other possible solutions
            remove_queen(row, col)
    return count
```

IDEA:

Call above function for row 0. Note that to place N queens in a NxN board you will need to place one in every row/col

Function above explores every column. Hence in the end you would have explored every cell in the row. If a placement works it moves to the next row. In a successful run you would have explored every row. If you reach a sucessful placement in the last row you increment count. 

If queen is not under attack in current col do nothing and move to next col

See that function returns count and backtracks it back to the first call only incrementing it if a solution is found

When not under attack we always remove the queen this is bc in both cases when  the resulting stack calls led to a solution or did not we want to move on to the exploring other possible solutions

