func dfsWordBreak(s string, words map[string]bool, cur string, res *[]string) {
	if s == "" {
		*res = append(*res, cur)
		return
	}

	sep := ""
	if len(cur) > 0 {
		sep = " "
	}

	for i := 1; i <= len(s); i++ {
		if words[s[:i]] {
			dfsWordBreak(s[i:], words, cur+sep+s[:i], res)
		}
	}
}

func wordBreak(s string, wordDict []string) []string {
	words := make(map[string]bool, len(wordDict))
	for _, word := range wordDict {
		words[word] = true
	}

	res := make([]string, 0)
	dfsWordBreak(s, words, "", &res)
	return res
}
