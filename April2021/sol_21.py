"""Triangle.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/
"""
from typing import List


class Solution:
    @staticmethod
    def browse(t):
        l = len(t)
        if l == 1:
            return t[0][0]
        t1 = [t[-2][i]+min(t[-1][i], t[-1][i+1]) for i in range(l-1)]
        while True:
            l1 = len(t1)
            if l1 == 1:
                return t1[0]
            t1 = [t[l1-2][i]+min(t1[i], t1[i+1]) for i in range(l1-1)]
            
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.browse(triangle)


test_cases = [
    [[2],[3,4],[6,5,7],[4,1,8,3]], 
    [[10]]
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.minimumTotal(case))
    print()
    print()
