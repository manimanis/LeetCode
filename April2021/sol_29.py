"""  Find First and Last Position of Element in Sorted Array.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3725/
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 0), [-1, -1]),
    (([1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3], 2), [3, 11])
]


class Solution:
    def binarySearch(self, nums, target, l, r):
        if len(nums) == 0:
            return -1
        p = -1
        while r >= l:
            m = (l + r) // 2
            if nums[m] == target:
                p = m
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return p

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        p = self.binarySearch(nums, target, 0, len(nums)-1)
        if p == -1:
            return [-1, -1]
        lp1, lp2 = p, p
        while True:
            p1 = self.binarySearch(nums, target, 0, lp1-1)
            if p1 != -1:
                lp1 = p1
            else:
                break
        while True:
            p2 = self.binarySearch(nums, target, lp2+1, len(nums)-1)
            if p2 != -1:
                lp2 = p2
            else:
                break
        return [lp1, lp2]



if __name__ == '__main__':
    make_tests(test_cases, Solution, 'searchRange')
