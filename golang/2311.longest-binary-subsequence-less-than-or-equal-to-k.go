func longestSubsequence(s string, k int) int {
	n := len(s)
	curLen, curVal := 0, 0
	zeros := 0

	for i := range n {
		if s[i] == '0' {
			zeros++
		}
	}

	for i := n - 1; i >= 0; i-- {
		switch s[i] {
		case '0':
			zeros--
		case '1':
			if curLen <= 30 {
				curVal += 1 << curLen
			} else {
				return curLen + zeros
			}
		}

		if curVal > k {
			return curLen + zeros
		}

		curLen++
	}

	return n
}
