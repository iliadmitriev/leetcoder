func findTheLongestSubstring(s string) int {
	mp := map[byte]int{
		'a': 0,
		'e': 1,
		'i': 2,
		'o': 3,
		'u': 4,
	}
	mask := 0
	maxLen := 0

	n := len(s)
	cache := map[int]int{0: -1}

	for i := 0; i < n; i++ {
		if _, ok := mp[s[i]]; ok {
			mask ^= (1 << mp[s[i]])
		}

		if j, ok := cache[mask]; ok {
			maxLen = max(maxLen, i-j)
		} else {
			cache[mask] = i
		}
	}

	return maxLen
}
