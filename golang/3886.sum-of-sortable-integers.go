func sortableIntegers(nums []int) int {

	n := len(nums)
	div := make([]int, 0)

	for d := 1; d*d <= n; d++ {
		if n%d == 0 {
			div = append(div, d)

			if n/d != d {
				div = append(div, n/d)
			}
		}
	}

	res := 0
	// indexes of the next descent moving from i onward to n
	nextDescent := make([]int, n)
	nextDescent[n-1] = n

	for i := n - 2; i >= 0; i-- {
		if nums[i] > nums[i+1] {
			nextDescent[i] = i
		} else {
			nextDescent[i] = nextDescent[i+1]
		}
	}

	isSortableWin := func(k int) bool {
		prev := 0

		for r := k - 1; r < n; r += k {
			l := r - k + 1
			drop := nextDescent[l] // first descent for left window border

			// case 1: window is sorted (no rotation is needed)
			if drop > r {
				// only need to connect to previous window
				if prev > nums[l] {
					return false
				}
				prev = nums[r]

			} else {
				// case 2: window has at least 1 descent at index drop
				// it's fixable if:
				// + no second descent within window
				// + joined window parts after rotation is sorted
				// + connects to previous window after rotation
				if nextDescent[drop+1] < r || prev > nums[drop+1] || nums[r] > nums[l] {
					return false
				}

				prev = nums[drop]
			}
		}

		return true
	}

	for _, d := range div {
		if isSortableWin(d) {
			res += d
		}
	}

	return res
}