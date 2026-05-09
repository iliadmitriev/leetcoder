func findMiddleIndex(nums []int) int {
	rightPart := 0
	for _, v := range nums {
		rightPart += v
	}

	leftPart := 0

	for i := 0; i < len(nums); i++ {
		rightPart -= nums[i]

		if leftPart == rightPart {
			return i
		}

		leftPart += nums[i]
	}

	return -1
}
