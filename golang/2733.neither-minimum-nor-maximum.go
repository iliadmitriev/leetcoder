func findNonMinOrMax(nums []int) int {
	maxItem, minItem := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] > maxItem {
			maxItem = nums[i]
		}
		if nums[i] < minItem {
			minItem = nums[i]
		}
	}

	for _, v := range nums {
		if v != maxItem && v != minItem {
			return v
		}
	}

	return -1
}
