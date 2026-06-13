class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        a = ord("a")
        z = ord("z")
        n = 26

        def worder(w: str) -> str:
            """map 'abcd' -> 'r'"""
            idx = sum(weights[ord(ch) - a] for ch in w) % n
            return chr(z - idx)

        return "".join(map(worder, words))
