import "strings"

func findOcurrences(text string, first string, second string) []string {
	res := make([]string, 0)

	words := strings.Split(text, " ")

	for i := 2; i < len(words); i++ {
		if words[i-2] == first && words[i-1] == second {
			res = append(res, words[i])
		}
	}

	return res
}
