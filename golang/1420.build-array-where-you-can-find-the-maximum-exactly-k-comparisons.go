const MOD = int(1e9) + 7

func numOfArrays(n int, m int, k int) int {

    // init cache
    cache := make([][][]int, n + 1)
    for i := 0; i <= n; i++ {
        cache[i] = make([][]int, m + 1)
        for j := 0; j <= m; j++ {
            cache[i][j] = make([]int, k + 1)
            for h := 0; h <= k; h++ {
                cache[i][j][h] = -1
            }
        }
    }
    // init base case
    for curMax := 0; curMax <= m; curMax++ {
        cache[n][curMax][0] = 1
    }

    var dp func (int, int, int) int
    dp = func(i, curMax, remain int) int {
        if i == n {
            if remain == 0 {
                return 1
            }
            return 0
        }
        if remain < 0 || m - curMax < remain {
            return 0
        }
        if cache[i][curMax][remain] != -1 {
            return cache[i][curMax][remain]
        }

        res := curMax * dp(i + 1, curMax, remain) % MOD;

        for j := curMax + 1; j <= m; j++ {
            res += dp(i + 1, j, remain - 1)
            res %= MOD
        }

        cache[i][curMax][remain] = res
        return res
    }

    return dp(0, 0, k)
}