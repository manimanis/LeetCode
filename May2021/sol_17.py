"""Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of English lowercase letters.
"""
from typing import List
from common.testcases import make_tests


test_cases = [
    ((["a","b","ba","bca","bda","bdca"],), 4),
    ((["xbc","pcxbcf","xb","cxbc","pcxbc"],), 5),
    ((["a","ab","ac","bd","abc","abd","abdd"],), 4)
]


class Solution:
    @staticmethod
    def find(words, word, l = None, r = None):
        if l is None or r is None:
            l, r = 0, len(words)-1
        if l <= r:
            m = (l + r) // 2
            if words[m] == word:
                return m
            ridx = -1
            if len(words[m]) >= len(word):
                ridx = Solution.find(words, word, m+1, r)
            if ridx == -1 and len(words[m]) <= len(word):
                return Solution.find(words, word, l, m-1)
            return ridx
        return -1

    @staticmethod
    def longest(word, words, map=None):
        #print(f"longest('{word}')")
        if word in map:
            return map[word]
        
        map[word] = 1
        wl = len(word)
        for j in range(wl):
            nw = word[:j] + word[j+1:]
            idx = Solution.find(words, nw)
            if idx != -1:
                #print(f"{nw} found at index {idx}")
                map[word] = max(map[word], 1 + Solution.longest(nw, words, map))
        return map[word]

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda str: len(str), reverse=True)
        #print(words)
        n = len(words)
        lss = 1
        i = 0
        self.map = {}
        while i < n:
            if words[i] is None:
                i += 1
                continue          
            lssw = Solution.longest(words[i], words, self.map)
            #print(f"= {lssw}")
            #print(f"map = {self.map}")
            if lssw > lss:
                lss = lssw
            i += 1
        return lss


if __name__ == '__main__':
    make_tests(test_cases, Solution, 'longestStrChain')