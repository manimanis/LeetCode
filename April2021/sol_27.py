"""Power of Three.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722/
"""
from common.testcases import make_tests


test_cases = [
    ((0,), False),
    ((27,), True),
    ((45,), False)
]


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'isPowerOfThree')
