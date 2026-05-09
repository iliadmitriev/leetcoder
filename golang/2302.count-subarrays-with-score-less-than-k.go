func countSubarrays(nums []int, k int64) int64 {
	total, cur := 0, 0
	limit := int(k)
	n := len(nums)

	for i, j := 0, 0; i < n; i++ {
		cur += nums[i]

		for cur*(i-j+1) >= limit {
			cur -= nums[j]
			j++
		}

		total += i - j + 1
	}

	return int64(total)
}
