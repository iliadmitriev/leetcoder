from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        dictSet = set(dictionary)
        minLen = min(len(word) for word in dictionary)
        maxLen = max(len(word) for word in dictionary)
        res = []

        for word in words:
            replacement = word

            for i in range(minLen, min(maxLen, len(word)) + 1):
                if word[:i] in dictSet:
                    replacement = word[:i]
                    break

            res.append(replacement)

        return " ".join(res)

