func checkDistances(s string, distance []int) bool {
	n := len(s)

	for i := 0; i < n; i++ {
		j := distance[s[i]-'a']
		right := i + j + 1
		left := i - j - 1

		if (left >= 0 && s[left] == s[i]) || (right < n && s[right] == s[i]) {
			continue
		}

		return false
	}

	return true
}
