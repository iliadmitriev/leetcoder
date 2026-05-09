class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res: list[str] = []

        def makeKey(word: str) -> tuple[int, ...]:
            key = [0] * 26

            for c in word:
                key[ord(c) - 97] += 1

            return tuple(key)

        prevKey = None
        for word in words:
            key = makeKey(word)
            if prevKey == key:
                continue
            else:
                prevKey = key
                res.append(word)

        return res

