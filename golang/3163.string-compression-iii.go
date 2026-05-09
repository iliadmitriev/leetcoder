func compressedString(word string) string {
	counter := 0
	var prev byte = 0
	res := bytes.NewBuffer(nil)

	for i := 0; i < len(word); i++ {
		if word[i] == prev && counter < 9 {
			counter++
		} else {
			if prev != 0 {
				res.WriteString(strconv.Itoa(counter))
				res.WriteByte(prev)
			}

			counter = 1
		}

		prev = word[i]
	}

	if prev != 0 {
		res.WriteString(strconv.Itoa(counter))
		res.WriteByte(prev)
	}

	return res.String()
}
