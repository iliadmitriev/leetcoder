
func maximumNumberOfStringPairs(words []string) int {
	mp := make(map[string]int, len(words))

	count := 0

	for _, word := range words {
		if _, ok := mp[string([]byte{word[1], word[0]})]; ok {
			count++
		}
		mp[word]++
	}

	return count
}
