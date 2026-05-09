func validPalindrome(s string) bool {

	var pal func(int, int, int) bool

	pal = func(i, j, r int) bool {
		for i < j {
			if s[i] == s[j] {
				i++
				j--
				continue
			}

			if r > 0 {
                return pal(i+1, j, 0) || pal(i, j-1, 0)
			}
            
			return false
		}

		return true
	}

    return pal(0, len(s) - 1, 1)
}