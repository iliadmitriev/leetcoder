func findKthBit(n int, k int) byte {
	if n == 0 {
		return '0'
	}

	inv := 0
	k--
	mid := 1<<(n-1) - 1

	for k > 0 {
		if k > mid {
			k = 2*mid - k
			inv++
		}

		mid /= 2
	}

	if inv%2 == 1 {
		return '1'
	}

	return '0'
}
