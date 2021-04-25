"""Count Binary Substrings.

https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = []
        lcar = None
        for car in s:
            if car != lcar:
                l.append(car)
            else:
                l[-1] += car
            lcar = car
        count = 0
        ll = len(l)
        for i in range(ll):
            count += min(len(l[i]), len(l[i-1]) if i - 1 >= 0 else 0)
            # count += min(len(l[i]), len(l[i+1]) if i + 1 < ll else 0)
        return count


test_cases = [
    "00110011",
    "10101"
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.countBinarySubstrings(case))
    print()
    print()