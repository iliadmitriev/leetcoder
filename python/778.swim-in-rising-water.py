class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, end = (0, 0), (m - 1, n - 1)
        Position = Tuple[int, int]

        def step(pos: Position, vis: Set[Position], max_water_level: int):
            phase = (-1, 0, 1, 0, -1)
            for i in range(4):
                next_pos = next_r, next_c = pos[0] + phase[i], pos[1] + phase[i + 1]
                if 0 <= next_r < m and 0 <= next_c < n and next_pos not in vis \
                        and grid[next_r][next_c] <= max_water_level:
                    yield next_r, next_c

        def check(max_water_level: int):
            vis = set()
            return dfs(start, vis, max_water_level)


        def dfs(pos: Position, visited: Set[Position], max_water_level: int):
            visited.add(pos)
            for next_pos in step(pos, visited, max_water_level):
                if next_pos == end:
                    return True
                if dfs(next_pos, visited, max_water_level):
                    return True

        left, right = grid[0][0], n * m - 1 
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left

        