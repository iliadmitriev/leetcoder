func isPalindrome(s string) bool {
	i, j := 0, len(s)-1

	for i < j {

		if s[i] != s[j] {
			return false
		}

		i++
		j--
	}

	return true
}

func dfsPalPart(res *[][]string, path []string, s string) {
	if len(s) == 0 {
		path_copy := make([]string, len(path))
		copy(path_copy, path)
		*res = append(*res, path_copy)
		return
	}

	for j := 1; j <= len(s); j++ {
		if isPalindrome(s[0:j]) {
			dfsPalPart(res, append(path, s[0:j]), s[j:])
		}
	}
}

func partition(s string) [][]string {
	res := [][]string{}
	dfsPalPart(&res, []string{}, s)
	return res
}
