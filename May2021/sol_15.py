"""
Valid Number

A valid number can be split up into these components (in order):

    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        At least one digit, followed by a dot '.'.
        At least one digit, followed by a dot '.', followed by at least one digit.
        A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    At least one digit.

For example, all the following are valid numbers: 
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", 
"53.5e93", "-123.456e789"], while the following are not valid numbers: 
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Example 4:

Input: s = ".1"
Output: true

 

Constraints:

    1 <= s.length <= 20
    s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
from common.testcases import make_tests

test_cases = [
    (("2",), True),
    (("0089",), True),
    (("-0.1",), True),
    (("+3.14",), True),
    (("4.",), True),
    (("-.9",), True),
    (("2e10",), True),
    (("-90E3",), True),
    (("3e+7",), True),
    (("+6e-1",), True),
    (("53.5e93",), True),
    (("-123.456e789",), True),
    (("abc",), False),
    (("1a",), False),
    (("1e",), False),
    (("e3",), False),
    (("99e2.5",), False),
    (("--6",), False),
    (("-+3",), False),
    (("95a54e53",), False),
    (("0..",), False),
    (("4e+",), False)
]

class Solution:
    @staticmethod
    def getSign(s: str, p: int, n: int) -> int:
        if p < n and s[p] in ['+', '-']:
            return p+1
        return p

    @staticmethod
    def getDigits(s: str, p: int, n: int) -> int:
        i = p
        while i < n and '0' <= s[i] <= '9':
            i += 1
        return i if i > p else p

    @staticmethod
    def getInteger(s: str, p: int, n : int) -> int:
        if p > n:
            return n
        p1 = Solution.getSign(s, p, n)
        p2 = Solution.getDigits(s, p1, n)
        return p2 if p2 > p1 else p
    
    @staticmethod
    def getDecimal(s: str, p: int, n:int) -> int:
        p1 = Solution.getInteger(s, p, n)
        is_decimal = p1 > p
        if not is_decimal:
            p1 = Solution.getSign(s, p, n) if p < n else p
            if p1 < n and s[p1] == '.':
                p2 = Solution.getDigits(s, p1+1, n)
                if p2 > p1+1:
                    return p2

        if is_decimal:
            if p1 < n and s[p1] == '.':
                p2 = Solution.getDigits(s, p1+1, n)
                if p2 >= p1+1:
                    return p2
            return p1
        
        return p

    def isNumber(self, s: str) -> bool:
        n = len(s)
        p = 0
        p1 = Solution.getDecimal(s, p, n)
        # print(p, p1, s[p:p1])
        if p1 >= n:
            return True

        if p1 > p and p1 < n and s[p1] in ['e', "E"]:
            p2 = Solution.getInteger(s, p1+1, n)
            # print(p, p1, p2, s[p:p2])
            if p2 == p1+1:
                return False

            if p2 == n:
                #print(s[p:p2])
                return True

        return False
            


if __name__ == '__main__':
    make_tests(test_cases, Solution, "isNumber")