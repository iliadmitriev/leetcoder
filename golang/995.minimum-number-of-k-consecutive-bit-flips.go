func minKBitFlips(nums []int, k int) int {
	n := len(nums)
	flipped := make([]bool, n)
	flips := 0
	inv := 0

	for i := 0; i < n; i++ {
		if i >= k && flipped[i-k] {
			inv = 1 - inv
		}

		if inv == nums[i] {
			if i+k > n {
				return -1
			}

			flips++
			flipped[i] = true
			inv = 1 - inv
		}
	}

	return flips
}
