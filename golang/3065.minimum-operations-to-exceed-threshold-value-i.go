
func minOperations(nums []int, k int) int {
	counter := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] < k {
			counter++
		}
	}

	return counter
}
