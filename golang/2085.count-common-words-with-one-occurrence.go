func countWords(words1 []string, words2 []string) int {
	set1 := make(map[string]int, len(words1))
	set2 := make(map[string]int, len(words2))

	for _, w := range words1 {
		set1[w]++
	}

	for _, w := range words2 {
		set2[w]++
	}

	count := 0

	for w, c := range set1 {
		if c == 1 && set2[w] == 1 {
			count++
			set1[w] = 0
			set2[w] = 0
		}
	}

	for w, c := range set2 {
		if c == 1 && set1[w] == 1 {
			count++
		}
	}

	return count
}
