func numJewelsInStones(jewels string, stones string) int {
	jew := make(map[rune]struct{}, len(jewels))

	for _, j := range jewels {
		jew[j] = struct{}{}
	}

	count := 0
	for _, s := range stones {
		if _, ok := jew[s]; ok {
			count++
		}
	}

	return count
}
