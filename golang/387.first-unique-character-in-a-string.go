func firstUniqChar(s string) int {
	const (
		base = 'a'
		size = 26
	)

	freq := [size]int{}
	pos := [size]int{}

	for i := range pos {
		pos[i] = -1
	}

	for i, c := range s {
		freq[c-base]++

		if pos[c-base] == -1 {
			pos[c-base] = i
		}
	}

	res := -1 // first met index of uniq
	for i := range size {
		if freq[i] != 1 {
			continue
		}

		if res == -1 || res > pos[i] {
			res = pos[i]
		}

	}

	return res
}