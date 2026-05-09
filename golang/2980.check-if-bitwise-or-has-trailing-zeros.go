func hasTrailingZeros(nums []int) bool {
	cnt := 0

	for _, num := range nums {
		cnt += 1 - num&1

		if cnt > 1 {
			return true
		}
	}

	return false
}
