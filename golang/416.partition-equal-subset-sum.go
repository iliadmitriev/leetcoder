func canPartition(nums []int) bool {
	total := 0

	for _, num := range nums {
		total += num
	}

	if total%2 != 0 {
		return false
	}

	target := total / 2

	dp := make([]bool, target+1)
	dp[0] = true

	for _, num := range nums {
		if dp[target] {
			return true
		}
		for i := target; i >= num; i-- {
			dp[i] = dp[i] || dp[i-num]
		}
	}

	return dp[target]
}
