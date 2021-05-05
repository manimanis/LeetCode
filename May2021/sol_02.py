"""Course Schedule III
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/"""
from typing import List
from common.testcases import make_tests
import heapq


test_cases = [
    (([[100,200],[200,1300],[1000,1250],[2000,3200]],), 3),
    (([[1,2]],), 1), 
    (([[3,2],[4,3]],), 0),
    (([[1,2],[2,3]],), 2),
    (([[5,5],[4,6],[2,6]],), 2),
    (([[5,11],[3,5],[10,20],[4,20],[10,16]],), 3),
    (([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]],),5)
]


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1]*100000+x[0])
        print(courses)
        td = 0
        pq = []
        for duration, lastday in courses:
            td += duration
            heapq.heappush(pq, -duration)
            print("push", pq, td)
            if td > lastday:
                td += heapq.heappop(pq)
                print("pop", pq, td)
        return len(pq)


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'scheduleCourse')