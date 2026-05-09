func findDuplicates(nums []int) []int {
	// use slice nums position as a marker than number have been met before
	// set number at index to negative
	res := []int{}
	for _, num := range nums {
		if nums[abs(num)-1] < 0 {
			res = append(res, abs(num))
		} else {
			nums[abs(num)-1] = -nums[abs(num)-1]
		}
	}

	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
