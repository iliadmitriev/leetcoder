func checkStrings(s1 string, s2 string) bool {
  const base = byte('a')

	counter := func(s string, start int) [26]int {

    n := len(s)
		m := [26]int{}

		for i := start; i < n; i += 2 {
			m[s[i] - base]++
		}

		return m
	}


	return (counter(s1, 0) == counter(s2, 0)) && (counter(s1, 1) == counter(s2, 1))
}