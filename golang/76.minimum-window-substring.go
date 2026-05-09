func minWindow(s string, t string) string {
	m, n := len(s), len(t)
	pattern := map[byte]int{} // symbol counts for a looked up pattern
	window := map[byte]int{}  // symbol counters for current window
	fulfilled := 0            // number of fulfilled symbols (if == n that current window is fulfill all symbols count for pattern)
	res := ""
	minRes := m + 1

	for i := range n {
		pattern[t[i]]++
	}

	i := 0
	for j := range m {
		c := s[j]

		window[c]++

		if window[c] <= pattern[c] {
			fulfilled++
		}

		for fulfilled == n && i <= j {
			if j-i+1 > 0 && minRes > j-i+1 {
				minRes = j - i + 1
				res = s[i : j+1]
			}

			d := s[i]
			if window[d] <= pattern[d] {
				fulfilled--
			}
			window[d]--
			i++
		}
	}

	return res
}