import "strings"

const SPACE = byte(' ')

func reorderSpaces(text string) string {
	res := strings.Builder{}
	words := make([]string, 0)
	spaces := 0
	j := 0
	n := len(text)

	for i := range n {
		if text[i] != SPACE {
			continue
		}

		spaces++
		if i > j {
			words = append(words, text[j:i])
		}

		j = i + 1
	}

	if j < n {
		words = append(words, text[j:n])
	}

	slots := len(words) - 1

	if slots == 0 {
		return words[0] + strings.Repeat(" ", spaces)
	}

	res.WriteString(words[0])

	separator := strings.Repeat(" ", spaces/slots)
	end := strings.Repeat(" ", spaces%slots)

	for i := 1; i < len(words); i++ {
		res.WriteString(separator)
		res.WriteString(words[i])
	}

	res.WriteString(end)

	return res.String()
}
