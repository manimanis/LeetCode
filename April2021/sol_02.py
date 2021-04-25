"""Ones and Zeroes.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3694/
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = sorted(strs, key=lambda s: len(s), reverse=True)
        print(strs)
        count = 0
        tnz, tno = m, n
        for s in strs:
            nz, no = 0, 0
            for car in s:
                if car == "0":
                    nz += 1
                else:
                    no += 1
            if nz <= tnz and no <= tno:
                tnz -= nz
                tno -= no
                count += 1
        return count


test_cases = [
    (["10","0001","111001","1","0"], 5, 3), # 4
    (["10","0","1"], 1, 1), # 2
    (["10","0001","111001","1","0"], 4, 3), # 3
    (["111","1000","1000","1000"], 9, 3) #3
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.findMaxForm(*case))
    print()
    print()