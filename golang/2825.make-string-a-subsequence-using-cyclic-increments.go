func canMakeSubsequence(str1 string, str2 string) bool {
	m, n := len(str1), len(str2)
	if m < n {
		return false
	}

	i, j := 0, 0

	for ; i < m && j < n && m-i >= n-j; i++ {
		if str2[j] == str1[i] || str2[j] == ((str1[i]-96)%26)+97 {
			j++
		}
	}

	if j == n {
		return true
	}

	return false
}
