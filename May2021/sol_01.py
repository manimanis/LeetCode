"""Prefix and Suffix Search
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/
"""
from typing import List


test_cases = [
    ((['apple'], 'a', 'e'), 0),
    ((["test", "atest", "tatest", "statest", "estatest", "testtetest"], "te", "t"), 5),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "bccbacbcba", "a"), 9),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "ab", "abcaccbcaa"), 4),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "a", "aa"), 5),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "cabaaba", "abaaaa"), 0),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "cacc", "accbbcbab"), 8),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "ccbcab", "bac"), 1),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "bac", "cba"), 2),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "ac", "accabaccaa"), 5),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "bcbb", "aa"), 3),
    ((["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
       "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"],
      "ccbca", "cbcababac"), 1)
]

class WordFilter:
    def __init__(self, words: List[str]):
        self.words = words
        
        n = len(words)
        # distinct words and their last positions
        dist_words = set(words)
        self.dist_words = {word: 0 for word in dist_words}
        for i in range(n):
            self.dist_words[words[i]] = i
        
        self.index = {}
        for word, position in self.dist_words.items():
            ps = (word[0], word[-1])
            if ps not in self.index:
                self.index[ps] = []
            self.index[ps].append(position)

    def f(self, prefix: str, suffix: str) -> int:
        maxlength, nw = -1, -1
        ps = (prefix[0], suffix[-1])
        if ps not in self.index:
            return -1
        wts = self.index[ps]
        #print(ps, wts)
        for i in range(len(wts)):
            word = self.words[wts[i]]
            if word.startswith(prefix) and word.endswith(suffix):
                if len(word) >= maxlength and wts[i] > nw:
                    maxlength = len(word)
                    nw = wts[i]
        return nw


if __name__ == '__main__':
    with open("May2021/testcases_01.txt") as f:
        lines = f.readlines()
        tc = eval(lines[1].replace('null', 'None'))
        out = eval(lines[2].replace('null', 'None'))
        exc = eval(lines[3].replace('null', 'None'))
    for i in range(1, len(tc)):
        test_cases.append(((tc[0][0], tc[i][0], tc[i][1]), exc[i]))
    # print(len(tc))
    # print(len(out))
    # print(len(exc))
    nerr = 2
    for inp, out in test_cases:
        filter = WordFilter(inp[0])
        res = filter.f(*inp[1:])
        if res != out:
            print(inp[0][(res-5 if res - 5 >= 0 else 0):(res+5 if res + 5 < len(inp[0]) else (len(inp[0])-1))])
            print(inp[1], inp[2])
            print(f"{res} != {out}")
            print()
            nerr -= 1
        if nerr <= 0:
            break
