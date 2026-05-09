func dominantIndex(nums []int) int {
	max1, max2 := nums[0], nums[1]
	max1Idx := 0
	if max1 < max2 {
		max1, max2 = max2, max1
		max1Idx = 1
	}

	for i := 2; i < len(nums); i++ {
		if nums[i] > max1 {
			max2 = max1
			max1 = nums[i]
			max1Idx = i
		} else if nums[i] > max2 {
			max2 = nums[i]
		}
	}

	if max1 >= 2*max2 {
		return max1Idx
	}

	return -1
}
