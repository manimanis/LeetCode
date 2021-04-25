"""Fibonacci Number.
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3709/
"""


class Solution:
    def fib(self, n: int) -> int:
        t = 0, 1
        if n < 2:
            return t[n]
        a, b = t
        for _ in range(n-1):
            a, b = b, a+b
        return b


test_cases = [
    0, 1, 2, 3, 4, 5
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.fib(case))
    print()
    print()