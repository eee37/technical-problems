class Solution:
    def tribonacci(self, n: int) -> int:
        return Solution.tribonacciHelper(n, [0] * max(n, 3))  # Max is needed to avoid error when assigning base cases

    @staticmethod
    def tribonacciHelper(n: int, tracker: list) -> int:
        if n < 0:
            return 0  # Review how to throw error

        tracker[0] = 0
        tracker[1] = 1
        tracker[2] = 1

        if 0 <= n <= 2:
            return tracker[n]

        for num in range(3, n):
            tracker[num] = tracker[num - 1] + tracker[num - 2] + tracker[num - 3]

        return tracker[n - 1] + tracker[n - 2] + tracker[n - 3]


    def tribonacci2(self, n: int) -> int:
        if n < 0:
            return 0

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1 # NOTE: Multi-assignemnt

        for num in range(3 , n):
            d = c + b + a

            # reassign
            a = b
            b = c
            c = d

        return c + b + a


sol = Solution()
# print(sol.tribonacci(4))
# print(sol.tribonacci(25))

print(sol.tribonacci2(4))
print(sol.tribonacci2(25))
