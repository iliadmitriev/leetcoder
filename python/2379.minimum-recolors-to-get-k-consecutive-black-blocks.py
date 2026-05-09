class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count("W")
        res = white

        for i in range(k, len(blocks)):
            white += blocks[i] == "W"
            white -= blocks[i - k] == "W"
            res = min(res, white)

        return res

