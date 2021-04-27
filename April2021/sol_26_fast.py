"""Furthest Building You Can Reach.
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3721/
"""
from typing import List
from queue import PriorityQueue


test_cases = [
    (([4, 2, 7, 6, 9, 14, 12], 5, 1), 4),
    (([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7),
    (([14, 3, 19, 3], 17, 0), 3),
    (([1, 2], 0, 0), 0),
    (([7, 5, 13], 0, 0), 1),
    (([14, 3, 19, 3], 17, 0), 3)
]


class Solution:
    """
    Greedy algorithm

    Principe
    Pour une solution O(n) on va utiliser le principe suivant :
    - Au début, à chaque fois, on utilise une échelle lorsqu'on a besoin de 
      monter
    - On sauvegarde en même temps le nombre de briques équivalent à chaque 
      échelle utilisée
    - Lorsque toutes les échelles sont épuisées :
      - On remplace les échelles par des briques, 
      - On préfère de remplacer les échelles qui sont équivalent à un nombre 
        minimal de briques

    Implémentation
    On utilise une 'priority queue' pour sauvegarder le nombre de briques 
    équivalent à une échelle.
    Lorsqu'on épuise toutes les échelles on retrouve la valeur minimale trouvée
    dans la 'priority queue' celle ci sera remplacée par des briques.
    Lorsque les briques sont épuisées nous avons allons atteint le point le plus
    éloigné.
    """

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = PriorityQueue()
        n = len(heights)
        for i in range(1, n):
            d = heights[i] - heights[i-1]
            if d > 0:
                pq.put(d)
                if pq.qsize() > ladders:
                    bricks -= pq.get()
                if bricks < 0:
                    return i-1
        return n-1


if __name__ == '__main__':
    sol = Solution()
    for inp, out in test_cases:
        print(inp)
        res = sol.furthestBuilding(*inp)
        print(f"{res} == {out} = {res == out}")
        print()
