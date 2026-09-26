import (
	"strings"
)

func evaluate(s string, knowledge [][]string) string {
	n := len(s)
	i := 0
	res := strings.Builder{}

	voc := make(map[string]string, len(knowledge))
	for _, kv := range knowledge {
		voc[kv[0]] = kv[1]
	}


	for j := 0; j <= n; j++ {
		if j == n || s[j] == '(' {
			term := s[i:j]
			res.WriteString(term)
      i = j + 1
		} else if s[j] == ')' {
			key := s[i:j]
			if value, ok := voc[key]; ok {
				res.WriteString(value)
			} else {
				res.WriteByte('?')
			}
			i = j + 1
		}
	}

	return res.String()
}