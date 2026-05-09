func replaceWords(dictionary []string, sentence string) string {
	dict := make(map[string]bool)
	minLen, maxLen := math.MaxInt, math.MinInt
	for _, word := range dictionary {
		dict[word] = true
		minLen = min(minLen, len(word))
		maxLen = max(maxLen, len(word))
	}

	res := make([]byte, 0, len(sentence))
	pos := false
	for i := 0; i < len(sentence); {
		if sentence[i] == ' ' {
			continue
		}
		j := i
		for j < len(sentence) && sentence[j] != ' ' {
			j++
		}

		replaced := false
		for k := i + minLen; k <= min(i+maxLen, len(sentence)); k++ {
			if dict[sentence[i:k]] {
				if pos {
					res = append(res, ' ')
				}

				res = append(res, sentence[i:k]...)
				pos = true
				replaced = true
				break
			}
		}

		if !replaced {
			if pos {
				res = append(res, ' ')
			}

			pos = true
			res = append(res, sentence[i:j]...)
		}

		i = j + 1
	}

	return string(res)
}
