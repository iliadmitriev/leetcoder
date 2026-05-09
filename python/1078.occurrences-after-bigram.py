class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        res = []

        w1, w2 = "", ""

        for word in text.split():
            if w2 == first and w1 == second:
                res.append(word)

            w2, w1 = w1, word

        return res

