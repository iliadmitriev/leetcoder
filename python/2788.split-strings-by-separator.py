class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        res: list[str] = []

        for word in words:
            res.extend(filter(None, word.split(separator)))

        return res

