"""Remove All Adjacent Duplicates in String II.
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3710/
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for car in s:
            if len(stk) == 0 or stk[-1][-1] != car:
                stk.append(car)
            else:
                stk[-1] += car
            if len(stk[-1]) == k:
                del stk[-1]
        return "".join(stk)


test_cases = [
    ("abcd", 2),
    ("deeedbbcccbdaa", 3),
    ("pbbcggttciiippooaais", 2)
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.removeDuplicates(*case))
    print()
    print()