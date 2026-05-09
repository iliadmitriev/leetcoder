func countConsistentStrings(allowed string, words []string) int {
	allowedMask := charBitask([]byte(allowed))

	count := 0

	for i := range words {

		if wordMask := charBitask([]byte(words[i])); wordMask&allowedMask == wordMask {
			count++
		}
	}

	return count
}

func charBitask(str []byte) int {
	res := 0

	for _, ch := range str {
		res |= 1 << (ch - 'a')
	}

	return res
}
