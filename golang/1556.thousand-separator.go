import (
	"strconv"
	"strings"
)

func thousandSeparator(n int) string {
	if n < 1000 {
		return strconv.Itoa(n)
	}
	res := strings.Builder{}

	for i := 1; n > 0; i++ {
		res.WriteByte(byte(n%10 + '0'))
		n /= 10

		if i%3 == 0 && n > 0 {
			res.WriteByte('.')
		}
	}

	b := []byte(res.String())
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
