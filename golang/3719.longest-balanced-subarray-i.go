func longestBalanced(nums []int) int {
	maxLen := 0

	for i := 0; i < len(nums); i++ {
		odd := make(map[int]struct{})
		even := make(map[int]struct{})

		for j := i; j < len(nums); j++ {

			if nums[j]%2 == 0 {
				even[nums[j]] = struct{}{}
			} else {
				odd[nums[j]] = struct{}{}
			}

			if len(odd) == len(even) {
				maxLen = max(maxLen, j-i+1)
			}
		}
	}

	return maxLen
}