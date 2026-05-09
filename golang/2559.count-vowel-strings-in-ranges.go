func vowelStrings(words []string, queries [][]int) []int {
	m, n := len(words), len(queries)
	res := make([]int, n)
	cache := make([]int, m+1)

	for i := 1; i <= m; i++ {
		cache[i] = cache[i-1] + startAndEndWithVowel(words[i-1][0], words[i-1][len(words[i-1])-1])
	}

	for j := 0; j < n; j++ {
		l, r := queries[j][0], queries[j][1]
		res[j] = cache[r+1] - cache[l]
	}

	return res
}

func startAndEndWithVowel(ch1, ch2 byte) int {
	if isVowelByte(ch1) && isVowelByte(ch2) {
		return 1
	}
	return 0
}

func isVowelByte(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
