import (
	"strings"
	"unicode"
)

func licenseKeyFormatting(s string, k int) string {
	cnt := 0
	tmp := strings.Builder{}
	ans := strings.Builder{}
	tmp.Grow(len(s))
	ans.Grow(len(s))

	for _, ch := range s {
		if ch != '-' {
			cnt++
			tmp.WriteRune(unicode.ToUpper(ch))
		}
	}

	w := tmp.String()

	rest := cnt % k

	if rest == 0 && cnt > 0 {
		rest = k
	}

	ans.WriteString(w[:rest])

	for i := rest; i < len(w); i += k {
		ans.WriteRune('-')
		ans.WriteString(w[i : i+k])
	}

	return ans.String()
}
