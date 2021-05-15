"""816. Ambiguous Coordinates
Medium

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.

 

Note:

    4 <= s.length <= 12.
    s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    (("(123)",), sorted(["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"])),
    (("(0123)",), sorted(["(0, 123)", "(0, 12.3)", "(0, 1.23)",
                          "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"])),
    (("(00011)",), sorted(["(0, 0.011)", "(0.001, 1)"]
                          ))
]


class OldSolution:
    @staticmethod
    def strip_zeros(word):
        length = len(word)
        if length == 1:
            return [word]
        if word[0] == '0' and word[-1] == '0':
            return None
        if word[0] == '0':
            return ['0' + '.' + word[1:]]
        if word[-1] == '0':
            return [word]
        res = [word]
        for i in range(1, length):
            res.append(word[:i] + '.' + word[i:])
        return res

    def ambiguousCoordinates(self, s: str) -> List[str]:
        length = len(s)
        s1 = s[1:-1]
        res = []
        for i in range(1, length - 2):
            left = Solution.strip_zeros(s1[:i])
            right = Solution.strip_zeros(s1[i:])
            if not left or not right:
                continue
            for l in left:
                for r in right:
                    res.append("({0}, {1})".format(l, r))
        return res


class Solution:
    @staticmethod
    def remove_zeros(s):
        n = len(s)
        if n == 1:
            yield s
        elif s[0] == s[-1] == '0':
            yield None
        elif s[0] == '0':
            yield s[0] + '.' + s[1:]
        elif s[-1] == '0':
            yield s
        else:
            yield s
            for i in range(1, n):
                yield s[:i] + '.' + s[i:]

    @staticmethod
    def all_pairs(word):
        n = len(word)
        for i in range(1, n):
            l = word[:i]
            r = word[i:]
            for lw in Solution.remove_zeros(l):
                for rw in Solution.remove_zeros(r):
                    yield lw, rw

    def ambiguousCoordinates(self, s: str) -> List[str]:
        length = len(s)
        s1 = s[1:-1]
        res = []
        for lw, rw in Solution.all_pairs(s1):
            if lw is None or rw is None:
                continue
            res.append(f"({lw}, {rw})")
        return res


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'ambiguousCoordinates',
               prepare_res=lambda l: sorted(l))
