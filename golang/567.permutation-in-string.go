func checkInclusion(s1 string, s2 string) bool {
	m, n := len(s1), len(s2)

	if m > n {
		return false
	}

	const SIZE = 26
	const BASE = 'a'

	pattern := [SIZE]int{}
	window := [SIZE]int{}

	for i := range m {
		pattern[s1[i]-BASE]++
		window[s2[i]-BASE]++
	}

	if window == pattern {
		return true
	}

	for i := m; i < n; i++ {
		window[s2[i]-BASE]++
		window[s2[i-m]-BASE]--

		if window == pattern {
			return true
		}

	}

	return false
}