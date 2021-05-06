"""Convert Sorted List to Binary Search Tree.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3733/
"""
from common.nodelist import TreeNode, ListNode
from common.testcases import make_tests


test_cases = [
    (([-10, -3, 0, 5, 9],), [0, -3, 9, -10, None, 5]),
    (([],), []),
    (([0],), [0]),
    (([1, 3], ), [3, 1]),
    (([1, 2, 3, 4, 5, 6, 7],), [4, 2, 6, 1, 3, 5, 7])
]


class Solution:
    @staticmethod
    def list_size(start, end=None):
        if start is None or start == end:
            return 0
        l = 1
        p = start
        while p.next != end:
            l += 1
            p = p.next
        return l

    @staticmethod
    def get_center(start, end=None):
        if start is None or start == end:
            return None
        mid = Solution.list_size(start, end) // 2
        p = start
        while mid > 0 and p.next != end:
            p = p.next
            mid -= 1
        return p

    def sortedListToBST(self, head: ListNode, right: ListNode = None) -> TreeNode:
        c = Solution.get_center(head, right)
        if c is not None:
            #print(c.val)
            node = TreeNode(c.val)
            #print()
            node.left = self.sortedListToBST(head, c)
            node.right = self.sortedListToBST(c.next, right)
            return node
        return None


if __name__ == '__main__':
    def prepare_data(arr):
        return (ListNode.build(arr),)

    def prepare_res(res):
        if res is not None:
            return res.toList()
        return []
    make_tests(test_cases, Solution, 'sortedListToBST',
               prepare_data, prepare_res)
