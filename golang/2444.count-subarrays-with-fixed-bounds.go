func countSubarrays(nums []int, minK int, maxK int) int64 {
	total := 0
	left, right := -1, -1
	cut := -1

	for i, num := range nums {
		if num < minK || num > maxK {
			left, right = -1, -1
			cut = i
		}

		if num == minK {
			left = i
		}

		if num == maxK {
			right = i
		}

		if left != -1 && right != -1 {
			total += min(left, right) - cut
		}
	}

	return int64(total)
}
