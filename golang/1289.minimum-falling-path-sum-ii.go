package main

func min_2_idx(arr []int) (int, int) {
	i1, i2 := 0, 1
	if arr[i1] > arr[i2] {
		i1, i2 = i2, i1
	}

	for i := 2; i < len(arr); i++ {
		if arr[i] < arr[i1] {
			i2 = i1
			i1 = i
		} else if arr[i] < arr[i2] {
			i2 = i
		}
	}

	return i1, i2
}

func minArr(arr []int) int {
	res := arr[0]
	for _, v := range arr {
		if v < res {
			res = v
		}
	}
	return res
}

func minFallingPathSum(grid [][]int) int {
	N := len(grid[0])

	if N == 1 {
		return grid[0][0]
	}

	dp := make([][]int, N)
	for r := range dp {
		dp[r] = make([]int, N)
	}
	for j := range dp[0] {
		dp[0][j] = grid[0][j]
	}

	for i := 1; i < N; i++ {
		j1, j2 := min_2_idx(dp[i-1])
		for j := range dp[i] {
			if j != j1 {
				dp[i][j] = dp[i-1][j1] + grid[i][j]
			} else {
				dp[i][j] = dp[i-1][j2] + grid[i][j]
			}
		}
	}

	return minArr(dp[N-1])
}
