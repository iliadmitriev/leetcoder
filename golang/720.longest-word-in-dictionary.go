func longestWord(words []string) string {
	if words == nil || len(words) == 0 {
		return ""
	}

	sort.Slice(words, func(i, j int) bool {
		if len(words[i]) == len(words[j]) {
			return words[i] > words[j]
		}
		return len(words[i]) < len(words[j])
	})

	if len(words[0]) != 1 {
		return ""
	}

	res := ""
	cache := make(map[string]bool, len(words)+1)
	cache[""] = true

	for _, word := range words {
		if _, ok := cache[word[:len(word)-1]]; ok {
			res = word
			cache[word] = true
		}
	}

	return res
}
