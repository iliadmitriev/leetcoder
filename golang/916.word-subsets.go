func wordSubsets(words1 []string, words2 []string) []string {
	res := make([]string, 0)
	cache := make(map[string]bool, len(words2))
	freq := [26]int{}

	for i := 0; i < len(words2); i++ {
		if cache[words2[i]] {
			continue
		}

		tmp := getCharCount(words2[i])
		for i := 0; i < 26; i++ {
			freq[i] = max(freq[i], tmp[i])
		}

		cache[words2[i]] = true
	}

	for i := 0; i < len(words1); i++ {
		tmp := getCharCount(words1[i])
		if isSubset(tmp, freq) {
			res = append(res, words1[i])
		}
	}

	return res
}

func getCharCount(word string) [26]int {
	v := [26]int{}
	for i := 0; i < len(word); i++ {
		v[word[i]-'a']++
	}
	return v
}

func isSubset(a [26]int, b [26]int) bool {
	for i := 0; i < 26; i++ {
		if a[i] < b[i] {
			return false
		}
	}
	return true
}
