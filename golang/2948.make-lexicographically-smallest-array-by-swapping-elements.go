func lexicographicallySmallestArray(nums []int, limit int) []int {
	N := len(nums)
	res := make([]int, N)
	posToGroup := make([]int, N)
	groupStart := []int{0}
	groupIdx := 0

	sorted := make([]int, N)
	for i := range sorted {
		sorted[i] = i
	}
	sort.Slice(sorted, func(i, j int) bool {
		return nums[sorted[i]] < nums[sorted[j]]
	})

	prev := nums[sorted[0]]
	for j := 0; j < N; j++ {
		i := sorted[j]
		num := nums[i]

		if num-prev > limit {
			groupStart = append(groupStart, j)
			groupIdx++
		}

		posToGroup[i] = groupIdx
		prev = num
	}

	for j := 0; j < N; j++ {
		i := posToGroup[j]
		res[j] = nums[sorted[groupStart[i]]]
		groupStart[i]++
	}

	return res
}
