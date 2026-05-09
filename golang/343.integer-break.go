func integerBreak(n int) int {
    cache := make([]int, n + 1)
    cache[0] = 0
    cache[1] = 1

    for i := 2; i <= n; i++ {
        for j := 1; j < i; j++ {
            cache[i] = max(cache[i], max(j * (i - j), j * cache[i - j]))
        }
    }


    return cache[n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}