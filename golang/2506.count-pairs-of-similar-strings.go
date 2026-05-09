func similarPairs(words []string) int {
	__key := func(s string) string {
		c := [26]int{}
		for i := 0; i < len(s); i++ {
			c[s[i]-'a']++
		}
		key := make([]byte, 0, 26)

		for i, v := range c {
			if v > 0 {
				key = append(key, byte('a'+i))
			}
		}
		return string(key)
	}

	res := 0
	seen := make(map[string]int)

	for _, w := range words {
		k := __key(w)
		if v, ok := seen[k]; ok {
			res += v
		}
		seen[k]++
	}

	return res
}
