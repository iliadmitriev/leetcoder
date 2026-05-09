func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	lo, hi := 0, nums[len(nums)-1]-nums[0]+1
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if smallestDistancePairCount(nums, mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}

func smallestDistancePairCount(nums []int, diff int) int {
	count := 0

	for left, right := 0, 1; right < len(nums); right++ {
		for nums[right]-nums[left] > diff {
			left++
		}

		count += right - left
	}

	return count
}
