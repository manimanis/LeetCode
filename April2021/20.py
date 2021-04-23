"""N-ary Tree Preorder Traversal.
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/
"""
from typing import List
from nodelist import Node


class Solution:
    @staticmethod
    def recursive(root: 'Node') -> List[int]:
        if root is None:
            return []
        l = [root.val]
        for node in root.children:
            l += Solution.recursive(node)
        return l
    
    @staticmethod
    def iterative(root: 'Node') -> List[int]:
        if root is None:
            return []
        l = [root.val]
        
        stk = [[-1, len(root.children), root.children]]
        while len(stk) > 0:
            if stk[-1][0]+1 < stk[-1][1]:
                cur_stk = stk[-1]
                cur_stk[0] += 1
                node = cur_stk[2][cur_stk[0]]
                l.append(node.val)
                stk.append([-1, len(node.children), node.children])
            else:
                stk.pop()
            
        return l
        
    
    def preorder(self, root: 'Node') -> List[int]:
        return Solution.iterative(root)