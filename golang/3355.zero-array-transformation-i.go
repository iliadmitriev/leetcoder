
func isZeroArray(nums []int, queries [][]int) bool {
	n := len(nums)
	prefix := make([]int, n+1)

	for _, q := range queries {
		prefix[q[0]]++
		prefix[q[1]+1]--
	}

	cur := 0
	for i := range n {
		cur += prefix[i]
		if cur < nums[i] {
			return false
		}
	}

	return true
}
