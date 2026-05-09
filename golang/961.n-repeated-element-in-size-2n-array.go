
func repeatedNTimes(nums []int) int {
	counter := make(map[int]int)

	for _, v := range nums {
		counter[v]++
		if counter[v] == 2 {
			return v
		}
	}

	return 0
}
