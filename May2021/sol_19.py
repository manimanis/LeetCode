"""Minimum Moves to Equal Array Elements II

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

 

Constraints:

    n == nums.length
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    (([1,2,3],), 2),
    (([1,10,2,9],), 16),
    (([1,0,0,8,6],), 14)
]


class Solution:
    def minMoves2(self, nums: List[int]) -> int: 
        nums.sort()    
        n = len(nums)
        m = nums[len(nums) // 2]
        s = sum(abs(v-m) for v in nums)
        # print(m, s)
        return s


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'minMoves2')
