"""Unique Paths II.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/
"""
from common.testcases import make_tests
from typing import List


test_cases = [
    (([[0, 0, 0], [0, 1, 0], [0, 0, 0]],), 2),
    (([[0, 1], [0, 0]],), 1),
    (([[0, 0, 0], [1, 0, 0], [0, 0, 0]],), 3),
    (([[1]],), 0)
]


class Solution:
    """
    Explication de la solution :
    Normalement il existe un seul chemin de la case de départ vers chacune des
    cases qui sont en première ligne ou en première colonne.

    Exemple avec une grille sans obstacles
    11111111
    1XXXXXXX
    1XXXXXXX
    1XXXXXXX

    Les 1 indiquent le nombre de chemin vers la cellule indiquée, les X 
    indiquent les cellules non encore visitées.

    Remplissage de la ligne numéro 2
    11111111
    12345678
    1XXXXXXX
    1XXXXXXX

    Le nombre de chemins qui mènent à une cellule vide dans la grille précédente
    peuvent être déduit à l'aide de la fonction suivante :
    nc(l, c) = nc(l-1, c) + nc(l, c-1)

    Lorsqu'il existent des obstacles ceux-ci pourront marqués par des 0. 

    Exemple
    1 1 1 1 1 1 1 1
    1 2 3 0 1 2 3 4
    1 0 3 3 4 6 913
    1 1 4 7 0 61528

    En utilisant la formule ci-dessus pour les cellules qui ne contiennent pas 
    des obstacles on fini par la matrice ci-dessus.

    On en déduit que le nombre de chemins qui mènent de (0, 0) à (n-1, m-1) est 
    28 chemins.
    """
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ng = [[(0 if grid[l][c] == 1 else -1)
               for c in range(n)] for l in range(m)]
        for l in range(m):
            for c in range(n):
                if ng[l][c] != 0:
                    if l == 0 and c == 0:
                        ng[l][c] = 1
                    elif l == 0:
                        ng[l][c] = ng[l][c-1]
                    elif c == 0:
                        ng[l][c] = ng[l-1][c]
                    else:
                        ng[l][c] = ng[l-1][c] + ng[l][c-1]
        return ng[m-1][n-1]


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'uniquePathsWithObstacles')

