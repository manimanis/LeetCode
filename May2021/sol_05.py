"""Jump Game II.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
    (([1, 1, 1, 1, 1],), 4),
    (([3, 3, 0, 0, 1],), 2), 
    (([6, 0, 1],), 1),
    (([0],), 0),
    (([1,2,3,4,5],), 3),
    (([4,1,1,3,1,1,1],), 2),
    (([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3],), 2)
]


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums = [min(i+nums[i], n-1) for i in range(n)]
        jumps = [-1] * n
        jumps[0], lv = 0, 0
        for i in range(n):
            j = nums[i]
            if jumps[j] == -1:
                lv = jumps[i] + 1
            while j > 0 and jumps[j] == -1:
                jumps[j] = lv
                j -= 1
        #print(jumps)
        return jumps[-1]
            
            


if __name__ == '__main__':
    make_tests(test_cases, Solution, "jump")
