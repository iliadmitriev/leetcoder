func maximumLength(s string) int {
	lo, hi := 0, len(s)
	var mid int
	res := 0

	for lo < hi {
		mid = (lo + hi) / 2
		if checkThriceLen(s, mid) {
			lo = mid + 1
			res = mid
		} else {
			hi = mid
		}
	}

	if res == 0 {
		return -1
	}

	return res
}

func checkThriceLen(s string, length int) bool {
	if length == 0 {
		return true
	}

	n := len(s)
	counter := make(map[byte]int, 26)

	for i := 0; i < n-length+1; i++ {
		if !checkSameSymbols(s, i, i+length) {
			continue
		}

		key := s[i]
		counter[key]++

		if counter[key] == 3 {
			return true
		}
	}

	return false
}

func checkSameSymbols(s string, start, end int) bool {
	key := s[start]
	for i := start + 1; i < end; i++ {
		if s[i] != key {
			return false
		}
	}

	return true
}
