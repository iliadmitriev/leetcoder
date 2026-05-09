

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        if len(strs) == 0:
            return 0

        rows = len(strs)
        cols = len(strs[0])
        marks = [False] * rows
        remove_count = 0

        for c in range(cols):
            removed = False
            for r in range(1, rows):
                if not marks[r] and strs[r - 1][c] > strs[r][c]:
                    remove_count += 1
                    removed = True
                    break

            if removed:
                continue

            for r in range(1, rows):
                if not marks[r] and strs[r - 1][c] < strs[r][c]:
                    marks[r] = True

        return remove_count

