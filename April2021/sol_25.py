"""Rotate Image.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3720/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            p = n - 2 * i
            if p <= 0:
                break
            vli = [matrix[i][j+i] for j in range(p)]
            vlni = [matrix[n-i-1][j+i] for j in range(p)]
            vci = [matrix[j+i][i] for j in range(p)]
            vcni = [matrix[j+i][n-i-1] for j in range(p)]
            for j in range(p):
                matrix[i+j][n-i-1] = vli[j]
                matrix[i+j][i] = vlni[j]
                matrix[i][i+j] = vci[p-j-1]
                matrix[n-i-1][i+j] = vcni[p-j-1]

