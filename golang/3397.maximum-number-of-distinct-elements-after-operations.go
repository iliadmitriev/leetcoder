func maxDistinctElements(nums []int, k int) int {
	// if k interval [-k, k] covers number of the elements
	// then in a worst case when all of the elements are equal
	// all this elements can be uniqualized
	if 2*k > len(nums) {
		return len(nums)
	}

	sort.Ints(nums)

	count := 0
	cur := nums[0] - k - 1 // lowest impossible element as current

	for _, num := range nums {
		x := min(num+k, max(num-k, cur+1))

		if cur < x {
			count++
		}

		cur = x
	}

	return count
}
