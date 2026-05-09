func minCapability(nums []int, k int) int {
	lo, hi := nums[0], nums[0]
	for _, num := range nums {
		lo = min(lo, num)
		hi = max(hi, num)
	}

	for mid := (lo + hi) / 2; lo < hi; mid = (lo + hi) / 2 {
		if checkGTE(nums, k, mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}

func checkGTE(nums []int, k int, cap int) bool {
	prev2, prev1, cur := 0, 0, 0

	for _, num := range nums {
		if num <= cap {
			prev2++
		}

		cur = max(prev2, prev1)
		if cur >= k {
			return true
		}

		prev2, prev1 = prev1, cur
	}

	return false
}
