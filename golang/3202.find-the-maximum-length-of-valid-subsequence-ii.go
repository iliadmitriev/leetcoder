func maximumLength(nums []int, k int) int {
	maxLen := 0

	dp := make([][]int, k)
	for i := range dp {
		dp[i] = make([]int, k)
	}

	for _, num := range nums {
		num %= k
		for j := range k {
			dp[num][j] = dp[j][num] + 1
			if dp[num][j] > maxLen {
				maxLen = dp[num][j]
			}
		}
	}

	return maxLen
}
