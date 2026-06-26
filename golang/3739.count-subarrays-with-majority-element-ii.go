func countMajoritySubarrays(nums []int, target int) int64 {
	n := len(nums)

	res := 0
	// running prefix, shifted by n + 1 to be always positive
	// and prefix of previous length should have smallest value to be positive
	pre := n + 1              // [-n;+n] -> [1; 2*n+1]
	cnt := make([]int, 2*n+2) // running prefix frequency
	acc := make([]int, 2*n+2)

	cnt[pre] = 1 // cnt[0] = 1
	acc[pre] = 1 // acc[0] = 1

	for _, num := range nums {
		if num == target {
			pre++
		} else {
			pre--
		}

		cnt[pre]++ // update prefix frequency
		// recalculate currect accumulated frequency
		// connecting it to previous length prefix
		// and current prefix frequency
		acc[pre] = acc[pre-1] + cnt[pre]

		res += acc[pre-1] // not inclusive
	}

	return int64(res)
}