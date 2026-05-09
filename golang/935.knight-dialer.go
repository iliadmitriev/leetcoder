const MOD = int(1e9) + 7;

func knightDialer(n int) int {

    dp := [2][10]int{
        [10]int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    }

    var cur, nxt int

    for i := 0; i < n - 1; i++ {
        cur = i % 2;
        nxt = (i + 1) % 2;

        dp[nxt][0] = (dp[cur][4] + dp[cur][6]) % MOD
        dp[nxt][1] = (dp[cur][6] + dp[cur][8]) % MOD
        dp[nxt][2] = (dp[cur][7] + dp[cur][9]) % MOD
        dp[nxt][3] = (dp[cur][4] + dp[cur][8]) % MOD
        dp[nxt][4] = (dp[cur][0] + dp[cur][3] + dp[cur][9]) % MOD
        dp[nxt][5] = 0
        dp[nxt][6] = (dp[cur][0] + dp[cur][1] + dp[cur][7]) % MOD
        dp[nxt][7] = (dp[cur][2] + dp[cur][6]) % MOD
        dp[nxt][8] = (dp[cur][1] + dp[cur][3]) % MOD
        dp[nxt][9] = (dp[cur][2] + dp[cur][4]) % MOD
    }

    res := 0;
    for i := 0; i < 10; i++ {
        res += dp[(n - 1) % 2][i];
        res %= MOD;
    }

    return res
}