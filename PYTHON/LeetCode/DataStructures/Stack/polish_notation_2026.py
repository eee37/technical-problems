class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b), # int truncates to zero
            "*": lambda a, b: a * b,
        }
        stack = []
        for item in tokens:
            print('----------------')
            print('item', item)
            print('stack', stack)
            if item == '+' or item == '-' or item == '*' or item == '/':
                # pop operation and last 2 ints
                right = stack.pop()
                left = stack.pop()
                print(left, item, right)
                op = operations[item]
                result = op(left, right)
                stack.append(result)
            else:
                stack.append(int(item)) # NOTE: items are strings need to convert to ints for ops to work
        return stack.pop()