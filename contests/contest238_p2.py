"""Frequency of the Most Frequent Element.
https://leetcode.com/contest/weekly-contest-238/problems/frequency-of-the-most-frequent-element/
"""
from typing import List


test_cases = [
    (([3, 3, 3], 5), 3),
    (([1, 2, 4], 5), 3),
    (([1, 4, 8, 13], 5), 2),
    (([3, 9, 6], 2), 1),
    (([
        9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982,
        9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994, 9937,
        9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916,
        9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907, 9913, 9916,
        9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981,
        9927, 9930, 9927, 9925, 9923, 9904, 9928, 9928, 9986, 9903,
        9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983,
        9973, 9917, 9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932,
        9964, 9972, 9935, 9946, 9966], 3056),
     73)
]


def solve1(t, k):
    # elems = sorted(set(t), reverse=True)
    dct = {}
    for elem in t:
        if elem not in dct:
            dct[elem] = 0
        dct[elem] += 1
    elems = sorted(dct.keys(), reverse=True)
    # print(elems, dct)
    maxcount = 0
    for elem in elems:
        ck = k
        count = 0
        for el in elems:
            if (elem - el) < 0:
                continue
            pts = elem - el
            weight = dct[el] * pts
            # print(f'el = {el} - pts = {pts} - weight = {weight} - ck = {ck}')
            if ck >= weight:
                count += dct[el]
                ck -= weight
            else:
                nb = ck // pts
                count += nb
                ck -= pts * nb
                # break
        # print(elem, count, ck)
        if count > maxcount:
            maxcount = count
    return maxcount


def solve2(t, k):
    n = len(t)
    t.sort()
    poids = [(0, 0)]

    for end in range(1, n):
        if t[end-1] != t[end]:
            poids.append((end, (t[end] - t[end-1]) * end + poids[-1][1]))
    poids.append((n, poids[-1][1]))
    print(poids)

    ck = k
    j = 0
    start, subpoids = 0, 0
    n2 = len(poids)
    while j < n2-1 and ck > 0:
        ck -= (poids[j][1] - subpoids)
        j += 1
    if ck < 0:
        diff = t[poids[j]] - t[start]
        ninc = abs(ck) // diff + int(abs(ck) % diff != 0)
        start += ninc
        subpoids += ninc * diff
    print(j, start, subpoids, ck)


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        return solve1(nums, k)


if __name__ == '__main__':
    sol = Solution()
    for inp, out in test_cases:
        print(inp)
        res = sol.maxFrequency(*inp)
        print(res)
        if res != out:
            print(f"Error should be {out}")
        print()
