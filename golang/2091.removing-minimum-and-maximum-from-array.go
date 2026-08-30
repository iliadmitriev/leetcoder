func minimumDeletions(nums []int) int {
	l, r := 0, 0
	m, M := nums[l], nums[r]
	n := len(nums)

	for i, x := range nums {
		if x < m {
			l = i
			m = x
		} else if x > M {
			r = i
			M = x
		}
	}

	if l > r {
		l, r = r, l
	}

	return min(
		l+1+n-r,
		min(
			r+1,
			n-l,
		),
	)
}