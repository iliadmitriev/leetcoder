func findKDistantIndices(nums []int, key int, k int) []int {
	indices := make([]int, 0)
	res := make([]int, 0)
	prev := 0

	for i, num := range nums {
		if num == key {
			indices = append(indices, i)
		}
	}

	for _, index := range indices {
		left := max(prev, index-k)
		right := min(len(nums), index+k+1)

		for j := left; j < right; j++ {
			res = append(res, j)
		}

		prev = right
	}

	return res
}
