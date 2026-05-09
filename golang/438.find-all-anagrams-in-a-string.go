func findAnagrams(s string, p string) []int {
	n := len(s)
	m := len(p)

	indices := make([]int, 0)

	pattern := [26]int{}
	cur := [26]int{}

	for i := range m {
		pattern[p[i]-'a']++
	}

	for i := range n {
		cur[s[i]-'a']++

		if i-m >= 0 {
			cur[s[i-m]-'a']--
		}

		if i+1-m >= 0 {
			if pattern == cur {
				indices = append(indices, i+1-m)
			}
		}

	}

	return indices
}