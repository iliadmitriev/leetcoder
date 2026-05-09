func minimizeMax(nums []int, p int) int {
	// optimization 1: trivial case
	if p == 0 {
		return 0
	}

	sort.Ints(nums)
	n := len(nums)

	// optimization 2: all pairs are used (no need to search minimal)
	if 2*p == n {
		imax := nums[1] - nums[0]

		for i := 2; i < n; i += 2 {
			imax = max(imax, nums[i+1]-nums[i])
		}
		return imax
	}

	check := func(threshould int) bool {
		count := 0
		for i := 0; i < n-1; i++ {
			if nums[i+1]-nums[i] <= threshould {
				count++
				i++
			}

			if count >= p {
				return true
			}
		}
		return false
	}

	lo, hi := 0, nums[n-1]-nums[0]

	for lo < hi {
		mid := (lo + hi) / 2

		if check(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
