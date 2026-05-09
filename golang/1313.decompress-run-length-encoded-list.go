func decompressRLElist(nums []int) []int {
	length := 0
	for i := 0; i < len(nums); i += 2 {
		length += nums[i]
	}

	res := make([]int, 0, length)

	for i := 0; i < len(nums); i += 2 {
		for j := 0; j < nums[i]; j++ {
			res = append(res, nums[i+1])
		}
	}

	return res
}
