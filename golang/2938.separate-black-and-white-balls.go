func minimumSteps(s string) int64 {
	swaps := 0

	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		for ; i < j && s[i] == '0'; i++ {
		}

		for ; i < j && s[j] == '1'; j-- {
		}

		swaps += j - i
	}

	return int64(swaps)
}
