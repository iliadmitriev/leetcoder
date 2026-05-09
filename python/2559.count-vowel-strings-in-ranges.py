class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        res = []

        n = len(words)
        acc = [0]

        for i in range(n):
            acc.append(acc[-1])

            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                acc[-1] += 1

        for left, right in queries:
            res.append(acc[right + 1] - acc[left])

        return res

