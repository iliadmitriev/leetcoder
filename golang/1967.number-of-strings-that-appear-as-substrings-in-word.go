func numOfStrings(patterns []string, word string) int {
	res := 0

	for _, pat := range patterns {
		if strings.Contains(word, pat) {
			res++
		}
	}

	return res
}