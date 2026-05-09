func countSubarrays(nums []int) int {
	total := 0
	n := len(nums)

	for i := 1; i < n-1; i++ {
		if 2*(nums[i-1]+nums[i+1]) == nums[i] {
			total++
		}
	}
	return total
}
