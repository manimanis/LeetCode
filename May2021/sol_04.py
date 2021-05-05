"""Non-decreasing Array
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    (([4, 2, 3],), True),
    (([4, 2, 1],), False),
    (([30, 25, 2, 1, 25],), False),
    (([25, 1, 2, 25, 30],), True),
    (([24, 25, 1, 2, 25, 30],), False),
    (([0, 0, 1, 25, 1, 2, 25, 30],), True),
    (([1, 2, 3, 4],), True),
    (([5, 7, 1, 8],), True),
    (([1],), True)
]


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        nc = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if nc == 1:
                    return False
                nc += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                print(nums)
        return True


if __name__ == '__main__':
    make_tests(test_cases, Solution, "checkPossibility")
