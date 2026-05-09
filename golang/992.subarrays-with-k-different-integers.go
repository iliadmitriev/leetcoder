func subarraysWithKDistinct(nums []int, k int) int {
	res := 0
	freq := make(map[int]int)

	for i, j, r := 0, 0, 0; r < len(nums); r++ {
		freq[nums[r]]++

		for len(freq) > k {
			freq[nums[j]]--
			if freq[nums[j]] == 0 {
				delete(freq, nums[j])
			}
			j++
			i = j
		}

		for ; freq[nums[j]] > 1; j++ {
			freq[nums[j]]--
		}

		if len(freq) == k {
			res += j - i + 1
		}

	}

	return res
}
