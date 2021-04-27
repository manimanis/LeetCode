"""Furthest Building You Can Reach.
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3721/
"""
from typing import List


class BinaryTree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def depth(self):
        ld, rd = 0, 0
        if self.right is not None:
            rd = 1 + self.right.depth()
        if self.left is not None:
            ld = 1 + self.left.depth()
        return max(rd, ld)

    def decrement(self, lval, rval, depth=0):
        ld, rd = 0, 0
        if self.right is not None:
            rd = 1 + self.right.decrement(lval, rval, depth+1)
        if self.left is not None:
            ld = 1 + self.left.decrement(lval, rval, depth+1)
        if self.right is None and self.left is None:
            #print(self.val)
            lt = (self.val[0] - lval, self.val[1])
            rt = (self.val[0], self.val[1] - rval)
            if lt[0] >= 0 and lt[1] >= 0:
                ln = BinaryTree(val=lt)
                self.left = ln
                ld += 1
            if rt[1] >= 0 and rt[0] >= 0:
                rn = BinaryTree(val=rt)
                self.right = rn
                rd += 1
        return max(ld, rd)

    def print(self):
        print(self.val)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

    
class Solution:
    """
    This solution time out for large arrays of data
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        root = BinaryTree(val=(bricks, ladders))
        lh = heights[0]
        inc = []
        n = len(heights)
        depth = 0
        for i in range(n):
            height = heights[i]
            if height > lh:
                depth = root.decrement(height-lh, 1)
                inc.append(i)
            lh = height
        
        # print(depth, inc)
        if depth == 0:
            start = inc[-1]-1
            for i in range(start+1, n):
                if heights[i] > heights[i-1]:
                    return i-1
            return n-1
        elif depth > len(inc):
            return n-1
        else:
            start = inc[depth-1]
            for i in range(start+1, n):
                if heights[i] > heights[i-1]:
                    return i-1
            return n-1

if __name__ == '__main__':
    test_cases = [
        (([4, 2, 7, 6, 9, 14, 12], 5, 1), 4),
        (([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7),
        (([14, 3, 19, 3], 17, 0), 3),
        (([1, 2], 0, 0), 0),
        (([7, 5, 13], 0, 0), 1),
        (([14,3,19,3], 17, 0), 3)
    ]
    sol = Solution()
    for inp, out in test_cases:
        print(inp)
        res = sol.furthestBuilding(*inp)
        print(f"{res} == {out} = {res == out}")
        print()