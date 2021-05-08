"""Super Palindromes.
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3736/
"""
from common.testcases import make_tests


test_cases = [
    (("4", "1000"), 4),
    (("1", "2"), 1),
    (("375259531", "1265368034085"), 18)
]


class Solution:
    @staticmethod
    def isPalindrome(v):
        v = str(v)
        i, j = 0, len(v) - 1
        while j > i and v[j] == v[i]:
            i, j = i+1, j-1
        return i >= j

    @staticmethod
    def buildPalindrome(size: int = 0) -> str:
        if size <= 1:
            return "1"
        if size == 2:
            return "11"
        return "1" + "0" * (size - 2) + "1"
    
    @staticmethod
    def nextPalindrome(pal: str = "") -> str:
        n = len(pal)
        if n == 0:
            return "1"
        if n == 1:
            if pal == "3":
                return Solution.buildPalindrome(n+1)
            return chr(ord(pal) + 1)
        if n == 2:
            if pal == "22":
                return Solution.buildPalindrome(n + 1)
            return "22"
        if pal == ("2" * n):
            return Solution.buildPalindrome(n + 1)

        s, inc = "", 1
        for i in range(n // 2, n):
            v = chr(ord(pal[i]) + inc)
            if v < "3":
                s += v
                inc = 0
            else:
                s += "0"
                inc = 1
        if n % 2 == 0:
            return s[::-1] + s
        return s[::-1] + s[1:]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        rleft = str(int(int(left) ** 0.5))
        rright = str(int(int(right) ** 0.5))
        ll, lr = len(rleft), len(rright)
        count = 0
        curr = Solution.buildPalindrome(ll)
        while len(curr) <= lr:
            lc = len(curr)
            if lc == ll and curr >= rleft:
                valid = lc != lr or (lc == lr and curr <= rright)
            elif lc == lr and curr <= rright:
                valid = lc != ll or (lc == ll and cur >= rleft)
            elif len(rleft) < len(curr) < len(rright):
                valid = True
            else:
                valid = False
            if valid:
                v = int(curr)
                if Solution.isPalindrome(v*v):
                    count += 1
            curr = Solution.nextPalindrome(curr)
        return count


if __name__ == '__main__':
    # for i in range(1000000000):
    #     if Solution.isPalindrome(i) and Solution.isPalindrome(i*i):
    #         print(i)
    make_tests(test_cases, Solution, 'superpalindromesInRange')