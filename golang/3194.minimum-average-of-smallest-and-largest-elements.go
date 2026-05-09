func minimumAverage(nums []int) float64 {
	n := len(nums)
	sort.Ints(nums)
	minAvg := float64(nums[0]+nums[n-1]) / 2.0

	for i := 1; i < n/2; i++ {
		minAvg = min(minAvg, float64(nums[i]+nums[n-i-1])/2.0)
	}

	return minAvg
}
