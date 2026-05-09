class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res: list[str] = []

        for word in words:
            row = set(word.lower())
            if row.issubset(row1) or row.issubset(row2) or row.issubset(row3):
                res.append(word)

        return res

