func removeAnagrams(words []string) []string {
	prevKey := [26]int{}
	res := make([]string, 0)

	for i := 0; i < len(words); i++ {
		key := __makeKey(words[i])
		if key != prevKey {
			res = append(res, words[i])
			prevKey = key
		}
	}

	return res
}

func __makeKey(s string) [26]int {
	key := [26]int{}
	for i := 0; len(s) > i; i++ {
		key[s[i]-'a']++
	}
	return key
}
