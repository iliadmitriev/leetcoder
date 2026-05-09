func minSwaps(nums []int) int {
	n := len(nums)
	window := 0
	for _, num := range nums {
		if num == 1 {
			window++
		}
	}
	ones := 0
	l := 0
	res := n - window

	for r := 0; r < 2*n; r++ {
		if nums[r%n] == 1 {
			ones++
		}

		if r-l+1 > window {
			if nums[l%n] == 1 {
				ones--
			}
			l++
		}

		if r-l+1 == window {
			res = min(res, window-ones)
		}
	}

	return res
}
