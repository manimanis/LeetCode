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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, arr):
        root = None
        for val in arr[::-1]:
            node = cls(val)
            node.next = root
            root = node
        return root

    def toList(self):
        arr = [self.val]
        p = self.next
        while p is not None:
            arr.append(p.val)
            p = p.next
        return arr
