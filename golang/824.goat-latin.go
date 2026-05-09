func toGoatLatin(sentence string) string {
	vowels := map[byte]struct{}{
		'a': {},
		'e': {},
		'i': {},
		'o': {},
		'u': {},
		'A': {},
		'E': {},
		'I': {},
		'O': {},
		'U': {},
	}

	isVowel := func(ch byte) bool {
		_, ok := vowels[ch]
		return ok
	}

	buff := strings.Builder{}

	n := len(sentence)
	extra := []byte{}

	for i, j := 0, 0; i < n; i = j + 1 {
		j = i
		for j < n && sentence[j] != ' ' {
			j++
		}

		word := sentence[i:j]

		if isVowel(word[0]) {
			buff.WriteString(word)
		} else {
			buff.WriteString(word[1:])
			buff.WriteByte(word[0])
		}
		buff.WriteString("ma")
		extra = append(extra, 'a')
		buff.Write(extra)

		if j < n {
			buff.WriteByte(' ')
		}
	}

	return buff.String()
}
