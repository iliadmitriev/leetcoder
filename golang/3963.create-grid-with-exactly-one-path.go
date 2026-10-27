func createGrid(m int, n int) []string {
    grid := make([][]byte, m)
    for r := range m {
        grid[r] = make([]byte, n)
        for c := range n {
            grid[r][c] = '#'
        }
    }

    slope := func(r, c int) int {
        w := m * r - c * n
        if w < 0 {
            return -w
        }
        return w
    }

    r, c := 0, 0
    grid[r][c] = '.'

    for r < m - 1 || c < n - 1 {
        if c == n - 1 || (r < m - 1 && slope(r + 1, c) <= slope(r, c + 1)) {
            r++
        } else {
            c++
        }

        grid[r][c] = '.'
    }

    res := make([]string, m)
    for r := range m {
        res[r] = string(grid[r])
    }
    return res
}