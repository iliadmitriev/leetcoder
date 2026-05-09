func maxUniqueSplit(s string) int {
	cache := make(map[string]bool)
	return backtrackSplit(s, cache, 0)
}

func backtrackSplit(s string, cache map[string]bool, start int) int {
	if start == len(s) {
		return len(cache)
	}

	counter := 0

	for i := start; i < len(s); i++ {
		key := string(s[start : i+1])
		if _, ok := cache[key]; ok {
			continue
		}

		cache[key] = true
		counter = max(counter, backtrackSplit(s, cache, i+1))
		delete(cache, key)
	}

	return counter
}
