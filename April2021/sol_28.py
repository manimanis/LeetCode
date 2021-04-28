"""Unique Paths II.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/
"""
from common.testcases import make_tests
from typing import List


test_cases = [
    (([[0, 0, 0], [0, 1, 0], [0, 0, 0]],), 2),
    (([[0, 1], [0, 0]],), 1),
    (([[0, 0, 0], [1, 0, 0], [0, 0, 0]],), 3),
    (([[1]],), 0)
]


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ng = [[(0 if grid[l][c] == 1 else -1)
               for c in range(n)] for l in range(m)]
        for l in range(m):
            for c in range(n):
                if ng[l][c] != 0:
                    if l == 0 and c == 0:
                        ng[l][c] = 1
                    elif l == 0:
                        ng[l][c] = ng[l][c-1]
                    elif c == 0:
                        ng[l][c] = ng[l-1][c]
                    else:
                        ng[l][c] = ng[l-1][c] + ng[l][c-1]
        return ng[m-1][n-1]


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'uniquePathsWithObstacles')

