func countBinarySubstrings(s string) int {
	count := 0
	v := [2]int{}
	prev := rune('#')
	i := 0

	for _, c := range s {
		if prev == c {
			v[i]++
		} else {
			count += min(v[0], v[1])
			i = 1 - i
			v[i] = 1
		}

		prev = c
	}

	return count + min(v[0], v[1])
}