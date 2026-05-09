func shortestToChar(s string, c byte) []int {
	n := len(s)
	res := make([]int, n)
	pos := -n

	for i := 0; i < n; i++ {
		if s[i] == c {
			pos = i
		}
		res[i] = i - pos // i always greater than pos
	}

	for i := n - 1; i >= 0; i-- {
		if s[i] == c {
			pos = i
		}
		res[i] = min(res[i], abs(pos-i))
	}

	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
