func countPairs(nums []int, target int) int {
	n := len(nums)
	sort.Ints(nums)
	count := 0

	for i, j := 0, n-1; i < j; {
		if nums[i]+nums[j] < target {
			count += j - i
			i++
		} else {
			j--
		}
	}

	return count
}
