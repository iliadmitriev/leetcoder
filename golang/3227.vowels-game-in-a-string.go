func doesAliceWin(s string) bool {
	// Alice can only loose if there is no vowels
	return slices.ContainsFunc([]byte(s), func(r byte) bool {
		return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u'
	})
}
