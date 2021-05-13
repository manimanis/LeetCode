"""Range Sum Query 2D - Immutable
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3740/


Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle defined 
    by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

    NumMatrix(int[][] matrix) Initializes the object with the integer 
    matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) 
    Returns the sum of the elements of matrix inside the rectangle defined 
    by its upper left corner (row1, col1) and lower right corner (row2, col2)


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -105 <= matrix[i][j] <= 105
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 104 calls will be made to sumRegion.

"""
from typing import List
from common.testcases import make_tests
from pprint import pprint


test_cases = [
    (([[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3]), 8),
    (([[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [1, 1, 2, 2]), 11),
    (([[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [1, 2, 2, 4]), 12)
]


class NumMatrix:
    @staticmethod
    def printMatrix(matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        nmat = [[0 for _ in range(m)] for _ in range(n)]
        for l in range(n):
            for c in range(m):
                nmat[l][c] = matrix[l][c]
                if l > 0:
                    nmat[l][c] += nmat[l-1][c]
                if c > 0:
                    nmat[l][c] += nmat[l][c-1]
                if l > 0 and c > 0:
                    nmat[l][c] -= nmat[l-1][c-1]
        self.nmat = nmat

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2c2 = self.nmat[row2][col2]
        r1c2 = self.nmat[row1-1][col2] if row1 > 0 else 0
        r2c1 = self.nmat[row2][col1-1] if col1 > 0 else 0
        r1c1 = self.nmat[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return r2c2 - r1c2 - r2c1 + r1c1


"""
Explication :
Prenons la matice suivante :
3 0 1 4 2
5 6 3 2 1
1 2 0 1 5
4 1 0 1 7
1 0 3 0 5
Figure 1, Matrice donnée

On veut calculer la somme des éléments de la sous-matrice, qui est égale à 8 :
2 0 1
1 0 1
0 3 0
Figure 2, Matrice à calculer

La méthode la plus simple et la plus intuitive est de faire deux compteurs
sur les lignes et les colonnes à additionner et le tour est joué.

Seulement, dans ce problème il s'agira de calculer plusieurs sommes de 
sous-matrices et cette méthode risque de "Time Out".

Il faudra, donc, chercher une autre méthode. J'ai pensé à faire le cumul de
toutes les cellules, ainsi on calcule pour chacune des cellules de cette matrice
mp[l, c] = somme(i=0..l, j=0..c, m[i, j])

On se retrouve donc avec l'exemple précédent avec la matrice suivante :
  3   3  4   8  10
[ 8] 14 18 [24] 27
  9  17 21  28  36
 13  22 26  34  49
[14] 23 30 [38] 58
Figure 3, Somme de matrice précalculée, mp

Ainsi, par exemple, 26 correspond à la somme de la sous-matrice :
3 0 1
5 6 3
1 2 0
4 1 0
Figure 4, mp[2, 3] = somme(i=0..2, j=0..3, m[i, j])

On peut remarquer que :
somme(i=r1..r2, j=c1..c2, m[i,j]) = 
  somme(i=0..r2, j=0..c2, m[i,j]) - 
  somme(i=0..r2, j=0..c1-1, m[i,j]) - 
  somme(i=0..r1-1, j=0..c2, m[i, j]) +
  somme(i=0..r1-1, j=0..c1-1, m[i, j]) =
    mp[r2, c2] - mp[r2, c1 - 1] - mp[r1-1, c2] + mp[r1-1, c1-1]

Comme nous avons déjà calculé toutes ces sommes, marqués dans la figure 3 entre 
[]. => 38 - 24 - 14 + 8 = 8
"""

if __name__ == '__main__':
    for inp, out in test_cases:
        matrix = NumMatrix(inp[0][0])
        res = matrix.sumRegion(*inp[1])
        if res != out:
            print("Error")
            print(inp)
            print(res, out)