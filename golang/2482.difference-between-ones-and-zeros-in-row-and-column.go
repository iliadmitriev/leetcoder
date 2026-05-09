func onesMinusZeros(grid [][]int) [][]int {
    m, n := len(grid), len(grid[0])
    row, col := make([]int, m), make([]int, n)

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                row[i]++
                col[j]++
            } else {
                row[i]--
                col[j]--
            }
        }
    }

    diff := make([][]int, m)
    for i := 0; i < m; i++ {
        diff[i] = make([]int, n)
        for j := 0; j < n; j++ {
            diff[i][j] = row[i] + col[j]
        }
    }
    return diff
}