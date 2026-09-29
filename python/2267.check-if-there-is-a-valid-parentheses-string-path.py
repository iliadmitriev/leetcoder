from functools import cache


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_len = m + n - 1

        # heuristics:
        # 1) path length must be even
        # 2) grid must not start with the closing parentheses
        # 3) grid must not end with the opening parentheses
        if path_len % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @cache
        def dfs(i, j, cnt) -> bool:
            if i == m or j == n:
                return False

            if grid[i][j] == "(":
                cnt += 1
            elif grid[i][j] == ")":
                cnt -= 1

            if cnt < 0:
                return False

            # heuristic 4:
            # there is not enough cells left to close the parentheses
            if cnt > m - i + n - j - 1:
                return False

            if i == m - 1 and j == n - 1:
                return cnt == 0

            return dfs(i + 1, j, cnt) or dfs(i, j + 1, cnt)

        return dfs(0, 0, 0)
