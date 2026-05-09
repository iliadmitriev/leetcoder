func rangeSum(nums []int, n int, left int, right int) int {
	const MOD = 1e9 + 7
	subs := make([]int, 0, n*(n-1)/2)

	for start := 0; start < n; start++ {
		sum := 0
		for i := start; i < n; i++ {
			sum += nums[i]
			subs = append(subs, sum)
		}
	}

	sort.Ints(subs)
	result := 0

	for i := left - 1; i < right; i++ {
		result = (result + subs[i]) % MOD
	}

	return result
}
