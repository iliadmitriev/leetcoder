func specialArray(nums []int) int {
	n := len(nums)
	counter := make([]int, n+1)

	for _, num := range nums {
		idx := min(num, n)
		counter[idx]++
	}

	total := 0
	for i := n; i >= 0; i-- {
		total += counter[i]
		if total == i {
			return i
		}
	}

	return -1
}
