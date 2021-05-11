"""Construct Target Array With Multiple Sums.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/
"""
from typing import List
from common.testcases import make_tests
from queue import PriorityQueue
import heapq


test_cases = [
    (([9,3,5],), True),
    (([1,1,1,2],), False),
    (([8, 5],), True),
    (([15,14,13,12],), False),
    (([5,2],), True),
    (([10,1],), True),
    (([1,100000],), True),
    (([1,1,2],), False),
    (([2],), False),
    (([1,1,61,9,17],), True)
]


class OldSolution:
    def isPossible(self, target: List[int]) -> bool:
        pq = PriorityQueue()
        for v in target:
            pq.put(-v)

        n = len(target)
        if n == 1:
            return target[0] == 1

        totsum = sum(target)
        while totsum > n:
            mxval = -pq.get()
            rsum = totsum - mxval
            if rsum > mxval:
                return False
            if rsum == 1:
                return True
            mxval %= rsum
            if mxval < 1:
                return False
            totsum = rsum + mxval
            pq.put(-mxval)

        return True


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        pq = [-v for v in target]
        heapq.heapify(pq)

        n = len(target)
        if n == 1:
            return target[0] == 1

        totsum = sum(target)
        while totsum > n:
            mxval = -heapq.heappop(pq)
            rsum = totsum - mxval
            if rsum > mxval:
                return False
            if rsum == 1:
                return True
            mxval %= rsum
            if mxval < 1:
                return False
            totsum = rsum + mxval
            heapq.heappush(pq, -mxval)

        return True

if __name__ == '__main__':
    make_tests(test_cases, Solution, 'isPossible')
