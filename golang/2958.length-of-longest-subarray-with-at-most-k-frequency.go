func maxSubarrayLength(nums []int, k int) int {
	res := 0
	freq := make(map[int]int)

	for i, j := 0, 0; j < len(nums); j++ {
		freq[nums[j]]++

		for ; i <= j && freq[nums[j]] > k; i++ {
			freq[nums[i]]--
		}

		res = max(res, j-i+1)
	}

	return res
}
