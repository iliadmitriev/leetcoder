
func minOperations(nums []int, k int) int {
	if k == 0 {
		return 0
	}

	total := 0
	for _, num := range nums {
		total += num
	}

	rem := total % k
	return (k + rem) % k
}
