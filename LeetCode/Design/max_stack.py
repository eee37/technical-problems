'''
    LC #716



     8 -> 7 -> 6

    None -> 9 -> 9 -> 9

    Initially didn't account for all cases of popMax. Shold run through more examples first.
    Consider dual list and heap for max approach: (value, index)  and stack/list

    Solution Notes:
        - Approach #1
            - Note that it has bugs view other user submited solutions instead
'''


class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0 or self.peekMax() < x:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.peekMax()))

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def peekMax(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]

    def popMax(self) -> int:
        if len(self.stack) > 0:
            max = self.peekMax()
            cur = self.stack[-1]

            to_add = []

            # remove non-max values
            while cur[0] != max:
                popped = self.stack.pop()
                to_add.append(popped[0])
                cur = self.stack[-1]  # NOTE: Want to set cur to next here

            # delete max
            max = self.stack.pop()

            # add nodes back in
            to_add.reverse()

            new_max = -sys.maxsize  # Error here. Will return popped max
            if len(self.stack) > 0:
                new_max = self.peekMax()

            for num in to_add:
                if num > new_max:
                    new_max = num
                self.stack.append((num, new_max))

            return max[0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()