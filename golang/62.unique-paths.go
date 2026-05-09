type cell struct {
    r, c int
}

func dp(i int, j int, cache map[cell]int) int {
    if i == 0 || j == 0 {
        return 1;
    }
    if value, ok := cache[cell{i, j}]; ok {
        return value
    }

    cache[cell{i, j}] = dp(i - 1, j, cache) + dp(i, j - 1, cache)
    return cache[cell{i, j}]
}

func uniquePaths(m int, n int) int {
    cache := make(map[cell]int, m)

    return dp(m - 1, n - 1, cache)
}