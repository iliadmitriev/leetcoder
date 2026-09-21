func resultArray(nums []int, k int) []int64 {
	if k == 1 {
		n := int64(len(nums))
		return []int64{n * (n + 1) / 2}
	}

	res := make([]int64, k)
	// k states:
	// i % 2 - current
	// 1 - i % 2 - previous
	dp := make([][2]int64, k)

	for i, num := range nums {
		// count the number's remainder
		dp[num%k][i%2]++

		// count the number's product remainder
		// using previous state 1 - i % 2
		for r := range k {
			if dp[r][1-i%2] > 0 {
				rk := num * r % k
				dp[rk][i%2] += dp[r][1-i%2]
			}
		}

		for r := range k {
			res[r] += dp[r][i%2]
			// reset state
			dp[r][1-i%2] = 0
		}
	}

	return res
}