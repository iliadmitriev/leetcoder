
func uncommonFromSentences(s1 string, s2 string) []string {
	words := make(map[string]int)
	res := []string{}

	for i, j := 0, 0; i <= len(s1); i++ {
		if i == len(s1) || s1[i] == ' ' {
			words[s1[j:i]]++
			j = i + 1
		}
	}

	for i, j := 0, 0; i <= len(s2); i++ {
		if i == len(s2) || s2[i] == ' ' {
			words[s2[j:i]]++
			j = i + 1
		}
	}

	for word, count := range words {
		if count == 1 {
			res = append(res, word)
		}
	}

	return res
}
