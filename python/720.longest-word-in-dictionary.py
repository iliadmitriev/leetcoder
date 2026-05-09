from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)

        cache = set([""])

        if not words or len(words[0]) != 1:
            return ""

        res = ""

        for word in words:
            if word[:-1] in cache:
                cache.add(word)
                res = word

        return res

