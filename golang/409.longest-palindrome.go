const N = 'z' - 'A' + 1

func longestPalindrome(s string) int {
	cnt := make([]int, N)
	for i := range s {
		cnt[s[i]-'A']++
	}

	res, mid := 0, 0
	for _, v := range cnt {
		res += v - v%2
		mid |= v % 2
	}

	return res + mid
}
