
func countPrefixes(words []string, s string) int {
	count := 0

	for i := 0; i < len(words); i++ {
		if startsWith(s, words[i]) {
			count++
		}
	}

	return count
}

func startsWith(s, t string) bool {
	return len(s) >= len(t) && s[:len(t)] == t
}
