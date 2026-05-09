func interpret(command string) string {
	res := strings.Builder{}

	for i := 0; i < len(command); i++ {
		switch command[i] {
		case 'G':
			res.WriteByte('G')
		case '(':
			switch command[i+1] {
			case ')':
				res.WriteByte('o')
				i++
			case 'a':
				res.WriteString("al")
				i += 3
			}
		}
	}

	return res.String()
}
