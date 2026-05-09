func getMinDistance(nums []int, target int, start int) int {
	n := len(nums)

	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	curMin := n

	for i := start; i < n && abs(i-start) < curMin; i++ {
		if nums[i] == target {
			curMin = abs(i - start)
		}
	}

	for i := start; i >= 0 && abs(i-start) < curMin; i-- {
		if nums[i] == target {
			curMin = abs(i - start)
		}
	}

	return curMin
}
