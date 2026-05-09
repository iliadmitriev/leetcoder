func countSubarrays(nums []int, k int) int64 {
	total := 0
	n := len(nums)
	maxItem, maxCount := 0, 0

	for i := range n {
		if nums[i] > maxItem {
			maxItem = nums[i]
		}
	}

	for i, j := 0, 0; i < n; i++ {
		if nums[i] == maxItem {
			maxCount++
		}

		for maxCount >= k {
			if nums[j] == maxItem {
				maxCount--
			}
			j++
		}

		total += j
	}

	return int64(total)
}
