"""Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],[
    "baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]



Constraints:

    1 <= products.length <= 1000
    There are no repeated elements in products.
    1 <= Σ products[i].length <= 2 * 10^4
    All characters of products[i] are lower-case English letters.
    1 <= searchWord.length <= 1000
    All characters of searchWord are lower-case English letters.

   Show Hint #1
Brute force is a good choice because length of the string is ≤ 1000.
   Show Hint #2
Binary search the answer.
   Show Hint #3
Use Trie data structure to store the best three matching. Traverse the Trie.
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    ((["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"), [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]),
    ((["bags", "baggage", "banner", "box", "cloths"], "bags"), [["baggage", "bags",
                                                                 "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]),
    ((["havana"], "havana"), [["havana"], ["havana"],
                              ["havana"], ["havana"], ["havana"], ["havana"]]),
    ((["havana"], "tatiana"), [[], [], [], [], [], [], []]),
    ((["abcde", "abcdef", "abcdefg"], "abfg"), [[], [], [], [], [], [], []])
]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def findByPrefix(products, word):
            first, last = 0, len(products) - 1
            while last >= first:
                m = (first + last) // 2
                if products[m].startswith(word):
                    ms, me = m, m
                    while ms - 1 >= first and products[ms-1].startswith(word):
                        ms -= 1
                    while me <= last and products[me].startswith(word):
                        me += 1
                    return ms, me
                elif products[m] > word:
                    last = m - 1
                else:
                    first = m + 1
            return -1, -1

        res = []
        products = sorted(products)
        n = len(searchWord)
        for i in range(1, n+1):
            subWord = searchWord[:i]
            fi, li = findByPrefix(products, subWord)
            products = products[fi:li]
            #print(subWord, fi, li, products)
            res.append(products[:min(len(products), 3)])                
        return res


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'suggestedProducts')

    import os

    with open(os.path.join(os.path.dirname(__file__), "testcases_31.txt"), 'r') as f:
        content = f.readlines()
        
    products = eval(content[0])
    word = eval(content[1])
    expected = eval(content[2])

    s = Solution()
    res = s.suggestedProducts(products, word)
    if res != expected:
        w = ""
        for car, r1, e1 in zip(word, res, expected):
            w += car
            if (r1 != e1):
                print(w)
                print('Result')
                print(r1)
                print('Expected')
                print(e1)
                print()
                input("Press Enter !")
