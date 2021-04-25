"""Palindrome Linked List.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/"""
from April2021.nodelist import ListNode


class Solution:
    @staticmethod
    def invert(head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nhead = Solution.invert(head.next)
        p1 = head
        p2 = head.next
        p3 = head.next.next
        p2.next = p1
        p1.next = p3
        return nhead

    @staticmethod
    def length(head: ListNode) -> int:
        p = head
        l = 0
        while p is not None:
            l += 1
            p = p.next
        return l

    @staticmethod
    def nodeAt(head: ListNode, index: int) -> ListNode:
        p = head
        l = 0
        while p is not None:
            if l == index:
                return p
            l += 1
            p = p.next
        return None

    def isPalindrome(self, head: ListNode) -> bool:
        # Déterminer la longueur de la liste
        l = Solution.length(head)

        if l <= 1:
            return True

        # Trouver le noeud qui se trouve juste avant le milieu
        before_mid = Solution.nodeAt(head, l // 2 + (l % 2 == 1) - 1)

        # Couper la liste en deux portions
        mid = before_mid.next
        before_mid.next = None

        # Inverser la deuxième portions
        mid2 = Solution.invert(mid)

        # Comparer les deux portions
        p1, p2 = head, mid2
        while p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


test_cases = [
    [1, 2, 2, 1],
    [1, 2],
    [1, 2, 2],
    [1, 1, 2, 1],
    [],
    [9],
    [7, 7]
]
sol = Solution()
for case in test_cases:
    lst = ListNode.build(case)
    print(case)
    print(sol.isPalindrome(lst))
    print()
    print()
