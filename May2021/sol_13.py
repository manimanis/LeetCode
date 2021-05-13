"""Construct Target Array With Multiple Sums.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/
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
