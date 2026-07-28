func smallestPalindrome(s string) string {
	var cnt [26]int

	n := len(s)
	mid := n / 2
	res := make([]byte, n)
	i := 0 // result insert position

	// find left half of the palindrome
	for i := 0; i < mid; i++ {
		cnt[s[i]-'a']++
	}

	for j := range 26 {
		cur := byte('a' + j)
		for range cnt[j] {
			res[i] = cur
			i++
		}
	}

	if n%2 == 1 {
		res[i] = s[mid]
		i++
	}

	for j := 25; j >= 0; j-- {
		cur := byte('a' + j)
		for range cnt[j] {
			res[i] = cur
			i++
		}
	}

	return string(res)
}