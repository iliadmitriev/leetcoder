func cherryPickup(grid [][]int) int {
    m, n := len(grid), len(grid[0])

    cur_dp, pre_dp := make([][]int, n), make([][]int, n)
    for i := range cur_dp {
        cur_dp[i] = make([]int, n)
        pre_dp[i] = make([]int, n)
    }

    dirs := [3]int{-1, 0, 1}

    for r := m - 1; r >= 0; r-- {
        for c1 := 0; c1 < n - 1; c1++ {
            for c2 := c1 + 1; c2 < n; c2++ {
                res := 0
                for _, d1 := range dirs {
                    for _, d2 := range dirs {
                        nc1, nc2 := c1 + d1, c2 + d2
                        if nc1 < 0 || nc2 >= n {
                            continue
                        }

                        res = max(res, pre_dp[nc1][nc2])
                    }
                }
                cur_dp[c1][c2] = grid[r][c1] + grid[r][c2] + res
            }
        }
        cur_dp, pre_dp = pre_dp, cur_dp
    }

    return pre_dp[0][n - 1]
}