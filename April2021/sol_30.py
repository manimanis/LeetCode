"""  Powerful Integers.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3726/"""
from typing import List
from common.testcases import make_tests


test_cases = [
    ((2, 3, 10), [2, 3, 4, 5, 7, 9, 10]),
    ((3, 5, 15), [2, 4, 6, 8, 10, 14]),
    ((2, 1, 10), [9, 2, 3, 5])
]


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powx, powy = [], []
        px, py = 1, 1
        while True:
            if px < bound:
                powx.append(px)
            if py < bound:
                powy.append(py)
            px *= x
            py *= y
            if ((x == 1) or (x > 1 and px > bound)) and ((y == 1) or (y > 1 and py > bound)):
                break

        res = set()
        for px in powx:
            for py in powy:
                if px + py <= bound:
                    res.add(px + py)
        return list(res)


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'powerfulIntegers')
