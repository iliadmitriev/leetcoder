class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        canWin = [True] * n
        for _, v in edges:
            canWin[v] = False

        champion = -1
        count = 0

        for u, win in enumerate(canWin):
            if not win:
                continue

            count += 1
            champion = u

        if count > 1:
            return -1

        return champion

