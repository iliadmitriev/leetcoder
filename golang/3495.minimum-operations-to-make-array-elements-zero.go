
func queryExp4Interval(a, b int) int {
	count := 0

	var left, right, prev, cur int

	prev = 1
	for d := 1; prev <= b; d += 1 {
		cur = 4 * prev

		left = max(a, prev)
		right = min(b, cur-1)

		if left <= right {
			count += d * (right - left + 1)
		}

		prev = cur
	}

	return (count + 1) / 2
}

func minOperations(queries [][]int) int64 {
	total := 0

	for _, q := range queries {
		total += queryExp4Interval(q[0], q[1])
	}

	return int64(total)
}
