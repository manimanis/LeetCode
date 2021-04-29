"""Maximum Building Height.
https://leetcode.com/contest/weekly-contest-238/problems/maximum-building-height/
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    ((5, [[2, 1], [4, 1]]), 2),
    ((6, []), 5),
    ((10, [[5, 3], [2, 5], [7, 4], [10, 3]]), 5),
    ((10, [[6, 2], [8, 4]]), 6),
    ((10, [[8, 5], [9, 0], [6, 2], [4, 0], [3, 2], [10, 0], [5, 3], [7, 3], [2, 4]]), 2)
]


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions) == 0:
            return n - 1
        restrictions.sort()
        nr = len(restrictions)

        x0, a0 = 0, -1
        for i in range(nr):
            restrictions[i][1] = min(
                restrictions[i][1], (restrictions[i][0] - x0) + a0)
            x0, a0 = restrictions[i]

        for i in range(nr-2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1], 
                -restrictions[i][0] + restrictions[i+1][0] + restrictions[i+1][1])

        mxb = 0
        x0, a0, a1 = 0, 0, 0
        for i in range(nr):
            r = restrictions[i]
            x1, b0 = r[0]-1, r[1]

            a1, b1 = a0 - x0, b0 + x1
            xmax = (b1 - a1) / 2
            ymax = min(int(xmax) + a1, int(-xmax) + b1)

            if ymax > mxb:
                mxb = ymax
            x0, a0 = x1, b0

        ymax = (n-1) + a0 - x0
        if ymax > mxb:
            mxb = ymax
        return mxb


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'maxBuilding')
