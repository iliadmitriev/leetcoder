func numIslands(grid [][]byte) int {
    m, n := len(grid), len(grid[0])

    var cleanup func(int, int)
    cleanup = func(i, j int) {
        if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == '0' {
            return
        }

        grid[i][j] = '0'
        cleanup(i + 1, j)
        cleanup(i, j + 1)
        cleanup(i - 1, j)
        cleanup(i, j - 1)
    }

    islands := 0
    for i := range m {
        for j := range n {
            if grid[i][j] == '0' {
                continue
            }

            cleanup(i, j)
            islands++
        }
    }

    return islands
}