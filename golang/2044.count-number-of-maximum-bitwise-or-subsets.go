func countMaxOrSubsets(nums []int) int {
	dp := make([]int, 1<<17)
	dp[0] = 1

	mask := 0

	for _, n := range nums {
		for i := mask; i >= 0; i-- {
			dp[i|n] += dp[i]
		}

		mask |= n
	}

	return dp[mask]
}
