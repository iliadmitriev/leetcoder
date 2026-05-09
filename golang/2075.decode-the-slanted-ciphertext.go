func decodeCiphertext(encodedText string, rows int) string {
	if rows == 1 {
		return encodedText
	}
	n := len(encodedText)
	cols := n / rows
	buf := strings.Builder{}

	for start := range cols {
		for i, j := 0, start; i < rows && j < cols; i, j = i+1, j+1 {
			buf.WriteByte(encodedText[i*cols+j])
		}
	}

	return strings.TrimRight(buf.String(), " ")

}