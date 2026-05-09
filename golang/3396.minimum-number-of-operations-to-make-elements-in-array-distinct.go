func minimumOperations(nums []int) int {
	count := make(map[int]int, 101)

	for i := len(nums) - 1; i >= 0; i-- {
		count[nums[i]]++
		if count[nums[i]] == 2 {
			return i/3 + 1
		}
	}
	return 0
}
