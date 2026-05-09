func frequencySort(nums []int) []int {
	ch := make(map[int]int, len(nums))

	for _, num := range nums {
		ch[num]++
	}

	sort.Slice(nums, func(i, j int) bool {
		return ch[nums[i]] < ch[nums[j]] || (ch[nums[i]] == ch[nums[j]] && nums[i] > nums[j])
	})

	return nums
}
