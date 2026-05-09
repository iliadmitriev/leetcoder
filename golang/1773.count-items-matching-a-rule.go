func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	types := map[string]int{"type": 0, "color": 1, "name": 2}
	curType := types[ruleKey]
	count := 0

	for i := range items {
		if items[i][curType] == ruleValue {
			count++
		}
	}

	return count
}
