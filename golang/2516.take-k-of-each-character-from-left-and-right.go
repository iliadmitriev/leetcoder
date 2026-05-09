func takeCharacters(s string, k int) int {
	n := len(s)
	cnt := make([]int, 3)
	for i := 0; i < n; i++ {
		cnt[s[i]-'a']++
	}

	need := make([]int, 3)
	for i := 0; i < 3; i++ {
		if cnt[i] < k {
			return -1
		}

		need[i] = cnt[i] - k
	}

	window := make([]int, 3)
	maxWindow := 0

	for i, j := 0, 0; i < n; i++ {
		window[s[i]-'a']++

		for window[0] > need[0] || window[1] > need[1] || window[2] > need[2] {
			window[s[j]-'a']--
			j++
		}

		maxWindow = max(maxWindow, i-j+1)
	}

	return n - maxWindow
}
