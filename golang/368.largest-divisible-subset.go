func largestDivisibleSubset(nums []int) []int {
	n := len(nums)
	dp, chain := make([]int, n), make([]int, n)
	idx := 0

	for i := range n {
		dp[i] = 1
		chain[i] = -1
	}

	sort.Ints(nums)

	for i := 1; i < n; i++ {
		for j := range i {
			if nums[i]%nums[j] == 0 {
				if dp[i] < dp[j]+1 {
					dp[i] = dp[j] + 1
					chain[i] = j
				}
			}

			if dp[i] > dp[idx] {
				idx = i
			}
		}
	}

	res := make([]int, 0, dp[idx])

	for ; idx != -1; idx = chain[idx] {
		res = append(res, nums[idx])
	}

	return res
}
