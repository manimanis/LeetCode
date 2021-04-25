"""Brick Wall
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3717/
"""
from typing import List


def wall(t):
    tset = {0: 0}
    for st in t:
        s = 0
        tset[0] += 1
        for v in st:
            s += v
            if s not in tset:
                tset[s] = 1
            else:
                tset[s] += 1
    l = len(t)
    nknots = sorted(tset.values())[:-2]
    if len(nknots) > 0:
        return l - nknots[-1]
    return l


class Solution:
    def leastBricks(self, t: List[List[int]]) -> int:
        return wall(t)


test_cases = [
    [[1, 2, 2, 1],
     [3, 1, 2],
     [1, 3, 2],
     [2, 4],
     [3, 1, 2],
     [1, 3, 1, 1]], 
    [[1, 1],
     [1, 1],
     [1, 1]],
    [[1000],
     [1000],
     [1000],],
    [[1, 9],
     [2, 8], 
     [3, 7]]
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.leastBricks(case))
    print()
    print()
