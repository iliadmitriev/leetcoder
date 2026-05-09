

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:

        def keyFunc(word: str) -> tuple[int, ...]:
            v = [0] * 26
            for ch in word.lower():
                if ch.isalpha():
                    v[ord(ch) - 97] += 1
            return tuple(v)

        def compareFunc(word1: tuple[int, ...], word2: tuple[int, ...]) -> bool:
            return all(f1 <= f2 for f1, f2 in zip(word1, word2))

        plate = keyFunc(licensePlate)

        words.sort(key=len)

        return next(word for word in words if compareFunc(plate, keyFunc(word)))

