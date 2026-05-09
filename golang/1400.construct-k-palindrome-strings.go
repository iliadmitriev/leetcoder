func canConstruct(s string, k int) bool {
	if len(s) < k {
		return false
	}

	if len(s) == k {
		return true
	}

	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
	}

	odd := 0
	for i := 0; i < 26; i++ {
		odd += count[i] % 2
	}

	return odd <= k
}
