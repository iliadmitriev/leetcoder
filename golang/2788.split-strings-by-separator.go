
func splitWordsBySeparator(words []string, separator byte) []string {
	res := make([]string, 0, len(words))
	for _, word := range words {
		for _, chunk := range splitStringByDelimiter(word, separator) {
			if len(chunk) == 0 {
				continue
			}

			res = append(res, chunk)
		}
	}

	return res
}

func splitStringByDelimiter(s string, delimiter byte) []string {
	res := make([]string, 0)

	i, j := 0, 0
	for i < len(s) {
		for j < len(s) && s[j] != delimiter {
			j++
		}

		if i < j {
			res = append(res, s[i:j])
		}

		i, j = j+1, j+1
	}

	return res
}
