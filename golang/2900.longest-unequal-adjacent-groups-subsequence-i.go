func getLongestSubsequence(words []string, groups []int) []string {
	res := make([]string, 0)
	prev := -1
	n := len(words)

	for i := range n {
		if groups[i] != prev {
			res = append(res, words[i])
			prev = groups[i]
		}
	}

	return res
}
