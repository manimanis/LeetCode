"""Delete Operation for Two Strings.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3734/


## Problem

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

### Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

### Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""
from common.testcases import make_tests


test_cases = [
    (("sea", "eat"), 2), 
    (("leetcode", "etco"), 4),
    (('abcd', 'dcba'), 6)
]


"""
Explication de la solution :

- On ajoute un espace au début de chacun des mots
- On compte, dans la première ligne, indice 0, et dans la première colonne, 
  le nombre de lettres à supprimer pour réduire chacun des mots à un seul espace.
- Dans la case (1, 1) on va calculer le nombre minimal de lettres à supprimer
  pour que " l" et " e" soient identiques, on devine aisement qu'il y a (2)
- Dans la case (1, 2) on va faire la même chose avec " le" et " e", on remarque
  que la lettre e est commune au deux chaines, on met donc (1)
- Dans la case (1, 3) on retrouve de nouveau la lettre "e" et on devra raisonner
  quelles sont les lettres à supprimer pour rendre " lee" identique à " e", 
  on devine aisément que c'est (2)
- On poursuit de la même façon dans toute la ligne 1
- Dans la ligne 2 il faudra deviner quel est le nombre de lettres à supprimer de
  " et" et toutes les sous-chaines de " leetcode" pour obtenir une même chaine.
- Après le remplissage de la matrice on remarque que pour rendre "leet" et "etco"
  il faudra supprimer 4 lettres
- La règle générale qui permet de remplir la matrice est la suivante, 
  on suppose que l indique le numéro de ligne et c le numéro de colonne :
  - remplir la ligne l = 0 par la valeur : mat[l][c] <- c
  - remplir la colonne c = 0 par la valeur de mat[l][c] <- l
  - pour l>0 et c>0
    - si word1[c] = word2[c] alors 
        mat[l][c] <- mat[l-1][c-1] 
      sinon 
        mat[l][c] = min(mat[l-1][c] + 1, mat[l][c-1] + 1)
  - retourner mat[n][m]

   0 1 2 3 4 5 6 7 8
     l e e t c o d e
0  0 1 2 3 4 5 6 7 8
1e 1 2 1 2 3 4 5 6 7
2t 2 3 2 3 2 3 4 5 6
3c 3 4 3 4 3 2 3 4 5
4o 4 5 4 5 4 3 2 3 4
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        n, m = len(word1), len(word2)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[i][j] = j
                elif j == 0 and i > 0:
                    dp[i][j] = i
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1)
        return dp[n-1][m-1]


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'minDistance')