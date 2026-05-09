import "strings"

func addSpaces(s string, spaces []int) string {
	words := make([]string, 0, len(spaces)+1)
	prev := 0
	spaces = append(spaces, len(s))
	n := len(spaces)

	for i := 0; i < n; i++ {
		words = append(words, s[prev:spaces[i]])
		prev = spaces[i]
	}

	return strings.Join(words, " ")
}
