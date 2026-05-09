const MOD = int(1e9) + 7

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
    cache := make(map[[3]int]int)
    
    var dp func(int,int,int) int
    dp = func (row, col, move int) int {
        if row < 0 || row >= m || col < 0 || col >= n {
            return 1
        }

        if move == 0 {
            return 0
        }

        key := [3]int{row, col, move}

        if value, ok := cache[key]; ok {
            return value
        }

        res := 0

        res += dp(row - 1, col, move - 1) % MOD
        res += dp(row + 1, col, move - 1) % MOD
        res += dp(row, col - 1, move - 1) % MOD
        res += dp(row, col + 1, move - 1) % MOD

        cache[key] = res % MOD
        return cache[key]
    }

    return dp(startRow, startColumn, maxMove)
}