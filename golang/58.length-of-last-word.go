func lengthOfLastWord(s string) int {
	cur := 0
	i := len(s) - 1

	for i >= 0 && s[i] == ' ' {
		i--
	}

	for i >= 0 && s[i] != ' ' {
		i--
		cur++
	}

	return cur
}
