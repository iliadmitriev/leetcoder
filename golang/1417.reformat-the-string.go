
func reformat(s string) string {
	digits, letters := make([]rune, 0), make([]rune, 0)
	for _, ch := range s {
		if '0' <= ch && ch <= '9' {
			digits = append(digits, ch)
		} else {
			letters = append(letters, ch)
		}
	}

	if len(digits) < len(letters) {
		digits, letters = letters, digits
	}

	if len(digits)-len(letters) > 1 {
		return ""
	}

	res := strings.Builder{}
	for i := range len(digits) + len(letters) {
		if i%2 == 0 {
			res.WriteRune(digits[0])
			digits = digits[1:]
		} else {
			res.WriteRune(letters[0])
			letters = letters[1:]
		}
	}

	return res.String()
}
