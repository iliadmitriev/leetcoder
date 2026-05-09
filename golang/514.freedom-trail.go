package main

import "math"

func findRotateSteps(ring string, key string) int {
	n, m := len(ring), len(key)

	ringToPos := make(map[byte][]int)
	for i := 0; i < n; i++ {
		ringToPos[ring[i]] = append(ringToPos[ring[i]], i)
	}

	dp := make([][]int, m+1)
	for r := range dp {
		dp[r] = make([]int, n+1)
	}

	for i := m - 1; i > 0; i-- {
		for _, k := range ringToPos[key[i-1]] {
            dp[i][k] = math.MaxInt
			for _, j := range ringToPos[key[i]] {
				step := 1 + min(abs(k-j), n-abs(k-j))
				dp[i][k] = min(dp[i][k], dp[i+1][j]+step)
			}
		}

	}

    for k := 0; k < n; k++ {
        dp[0][k] = math.MaxInt
		for _, j := range ringToPos[key[0]] {
			step := 1 + min(abs(k-j), n-abs(k-j))
			dp[0][k] = min(dp[0][k], dp[1][j]+step)
		}
    }

	return dp[0][0]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
