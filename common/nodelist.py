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

    def __str__(self):
        return str(self.toList())

    def __repr__(self):
        return str(self.toList())


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build(cls, arr, idx=0):
        if idx < len(arr):
            node = cls(arr[idx])
            node.left = TreeNode.build(arr, 2*idx+1)
            node.right = TreeNode.build(arr, 2*idx+2)
            return node
        return None

    def toList(self, lst=None, idx=0):

        def expand_list(lst, idx):
            while idx >= len(lst):
                lst.append(None)

        if lst is None:
            lst = []
        expand_list(lst, idx)
        lst[idx] = self.val

        if self.left is not None and self.right is not None:
            expand_list(lst, idx*2+2)
            self.left.toList(lst, idx*2+1)
            self.right.toList(lst, idx*2+2)
        elif self.left is not None:
            expand_list(lst, idx*2+2)
            self.left.toList(lst, idx*2+1)
            lst[idx*2+2] = None
        elif self.right is not None:
            expand_list(lst, idx*2+2)
            lst[idx*2+1] = None
            self.right.toList(lst, idx*2+2)
        if len(lst) > 0 and lst[-1] == None:
            return lst[:-1]
        return lst

    def __str__(self):
        return str(self.toList())

    def __repr__(self):
        return str(self.toList())


if __name__ == '__main__':
    l = TreeNode.build([4, 2, 6, 1, 3, 5, 7])
    print(l.toList())
    l = TreeNode.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(l.toList())
    for i in range(1, 16):
        l1 = [j for j in range(1, i+1)]
        tn = TreeNode.build(l1)
        l2 = tn.toList()
        if l1 != l2:
            print('Error', i, l1, l2)
        else:
            print("Ok", i, l1)
    l = TreeNode.build([0, -3, 9, -10, None, 5])
    print(l.toList())
