

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        def find_sub_island(
            row: int,
            col: int,
            grid1: list[list[int]],
            grid2: list[list[int]],
            visited: list[list[bool]],
        ) -> bool:
            M, N = len(grid1), len(grid1[0])

            visited[row][col] = True

            is_sub_island = grid1[row][col] == 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nRow, nCol = row + dr, col + dc

                if (
                    0 <= nRow < M
                    and 0 <= nCol < N
                    and not visited[nRow][nCol]
                    and grid2[nRow][nCol] == 1
                ):
                    next_is_sub_island = find_sub_island(
                        nRow, nCol, grid1, grid2, visited
                    )
                    is_sub_island &= next_is_sub_island

            return is_sub_island

        M, N = len(grid1), len(grid1[0])
        visited = [[False] * N for _ in range(M)]

        sub_islands = 0
        for r in range(M):
            for c in range(N):
                if not visited[r][c] and grid2[r][c] == 1:
                    sub_islands += find_sub_island(r, c, grid1, grid2, visited)

        return sub_islands

