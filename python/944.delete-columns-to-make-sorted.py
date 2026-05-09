class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deleted = 0

        cols = len(strs[0])
        rows = len(strs)

        for c in range(cols):
            for r in range(1, rows):
                if strs[r - 1][c] > strs[r][c]:
                    deleted += 1
                    break

        return deleted

