# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    
    @classmethod
    def build(cls, arr):
        root = None
        for val in arr:
            node = cls(val)
            if root is None:
                root = node
            