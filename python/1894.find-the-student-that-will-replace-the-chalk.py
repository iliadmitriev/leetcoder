class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:

        k %= sum(chalk)

        for i, ch in enumerate(chalk):
            if k < ch:
                return i
            k -= ch

        return 0

