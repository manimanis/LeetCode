"""
1855. Maximum Distance Between a Pair of Values

    User Accepted: 3304
    User Tried: 4463
    Total Accepted: 3400
    Total Submissions: 9432
    Difficulty: Medium

You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, 
is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid 
pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

 

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).

Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).

Example 4:

Input: nums1 = [5,4], nums2 = [3,2]
Output: 0
Explanation: There are no valid pairs, so return 0.

 

Constraints:

    1 <= nums1.length <= 105
    1 <= nums2.length <= 105
    1 <= nums1[i], nums2[j] <= 105
    Both nums1 and nums2 are non-increasing.
"""
from common.testcases import make_tests
from typing import List


test_cases = [
    (([55,30,5,4,2], [100,20,10,10,5]), 2),
    (([2,2,2], [10,10,1]), 1),
    (([30,29,19,5], [25,25,25,25,25]), 2),
    (([5,4], [3,2]), 0)
]


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, k = 0, 0, 0
        n1, n2 = len(nums1), len(nums2)
        nums = []
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                nums.append((1, i, nums1[i]))
                i += 1
            else:
                nums.append((2, j, nums2[i]))
                j += 1
        for l in range(i, n1):
            nums.append((1, l, nums1[l]))
        for l in range(j, n1):
            nums.append((1, l, nums2[l]))
        print(nums)


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'maxDistance')