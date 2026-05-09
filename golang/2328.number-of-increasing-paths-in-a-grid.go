import (
    "sort"
)

const MOD = int(1e9) + 7

func countPaths(grid [][]int) int {

    m, n := len(grid), len(grid[0])
    // create all cells
    cells := make([][2]int, 0, m * n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            cells = append(cells, [2]int{i, j})
        }
    }
    // sort all cells accordint to grid value
    sort.Slice(cells, func(i, j int) bool {
        return grid[cells[i][0]][cells[i][1]] < grid[cells[j][0]][cells[j][1]]
    })

    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = 1
        }
    }

    steps := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    var i, j, ni, nj int
    for _, cell := range cells {
        i, j = cell[0], cell[1]
        for _, step := range steps {
            ni, nj = i + step[0], j + step[1]

            if 0 <= ni && ni < m && 0 <= nj && nj < n && grid[i][j] < grid[ni][nj] {
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= MOD
            }
        }
    }

    res := 0
    for i := range dp {
        for j := range dp[i] {
            res += dp[i][j]
            res %= MOD
        }
    }

    return res
}