func minimumCost(nums []int) int {

	minA, minB := nums[1], nums[2]

	if minA > minB {
		minA, minB = minB, minA
	}

	for i := 3; i < len(nums); i++ {
		if minA > nums[i] {
			minB, minA = minA, nums[i]
		} else if minA == nums[i] || minB > nums[i] {
			minB = nums[i]
		}
	}

	return nums[0] + minA + minB
}