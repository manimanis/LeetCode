"""
Let's consider an infinite sequence of digits constructed of ascending 
powers of 10 written one after another. Here is the beginning of the 
sequence: 110100100010000… You are to find out what digit is located at 
the definite position of the sequence.

Input
There is the only integer N in the first line (1 ≤ N ≤ 65535). 
The i-th of N left lines contains the integer Ki — the number of position in 
the sequence (1 ≤ Ki ≤ 2^31 − 1).

Output
You are to output N digits 0 or 1 separated with a space. 
More precisely, the i-th digit of output is to be equal to the Ki-th digit 
of described above sequence.
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    ((3,), 0),
    ((14,), 0),
    ((7,), 1),
    ((6,), 0),
    ((2147483647,), 0)
]


class Solution:
    def answer(self, n):
        ni = ((8*n-7)**0.5 - 1) / 2
        return 1 if (ni == int(ni)) else 0


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'answer')


