import (
	"strings"
)

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}

	sign := num < 0
	if sign {
		num = -num
	}

	tmp := strings.Builder{}

	for num > 0 {
		tmp.WriteByte('0' + byte(num%7))
		num /= 7
	}

	if sign {
		tmp.WriteRune('-')
	}

	res := tmp.String()

	// reverse result string
	n := len(res)
	ans := make([]byte, n)
	for i := n - 1; i >= 0; i-- {
		ans[n-1-i] = res[i]
	}

	return string(ans)
}
