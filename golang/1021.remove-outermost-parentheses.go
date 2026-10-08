import (
	"strings"
)

func removeOuterParentheses(s string) string {
	d := 0
	sb := strings.Builder{}

	for _, ch := range s {
		switch {
		case ch == '(' && d > 0:
			{
				sb.WriteRune(ch)
			}
		case ch == ')' && d > 1:
			{
				sb.WriteRune(ch)
			}
		}

		switch ch {
		case '(':
			{
				d++
			}
		case ')':
			{
				d--
			}

		}
	}

	return sb.String()
}