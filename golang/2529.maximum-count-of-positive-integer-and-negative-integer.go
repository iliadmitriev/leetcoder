func maximumCount(nums []int) int {
	n := len(nums)

	if nums[0] > 0 {
		return n
	}

	if nums[n-1] < 0 {
		return n
	}

	zeroIns := leftBinSearch(nums, 0)
	oneIns := rightBinSearch(nums, 0)

	return max(zeroIns, n-oneIns)
}

func leftBinSearch(arr []int, x int) int {
	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return lo
}

func rightBinSearch(arr []int, x int) int {
	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] <= x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return lo
}
