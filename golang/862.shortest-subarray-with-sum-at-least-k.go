
type minHeapQ [][2]int

func shortestSubarray(nums []int, k int) int {
	minLen := len(nums) + 1

	q := make(minHeapQ, 0, len(nums))
	q = append(q, [2]int{0, -1})

	cur := 0
	for i, num := range nums {
		cur += num

		for len(q) > 0 && q[len(q)-1][0] >= cur {
			q = q[:len(q)-1]
		}

		q = append(q, [2]int{cur, i})

		for len(q) > 0 && cur-q[0][0] >= k {
			minLen = min(minLen, i-q[0][1])
			q = q[1:]
		}
	}

	if minLen > len(nums) {
		return -1
	}

	return minLen
}
