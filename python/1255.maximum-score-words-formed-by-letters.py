from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        chars = Counter(letters)
        scores = {chr(i + 97): s for i, s in enumerate(score)}

        def checkWord(word: str, letters: Counter) -> bool:
            for ch, cnt in Counter(word).items():
                if ch not in letters or letters[ch] < cnt:
                    return False
            return True

        def countWordScore(word: str, letters: Counter, scores: dict[str, int]) -> int:
            res = 0
            for ch in word:
                letters[ch] -= 1
                res += scores[ch]
            return res

        def appendLetters(word: str, letters: Counter) -> None:
            for ch in word:
                letters[ch] += 1

        def dfs(i: int, score: int, letters: Counter, scores: dict[str, int]) -> int:
            if i == len(words):
                return score

            res = dfs(i + 1, score, letters, scores)

            if checkWord(words[i], chars):
                count = countWordScore(words[i], chars, scores)
                res = max(res, dfs(i + 1, score + count, letters, scores))
                appendLetters(words[i], chars)

            return res

        return dfs(0, 0, chars, scores)

