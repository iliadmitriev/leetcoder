import "bytes"

func longestDiverseString(a int, b int, c int) string {
	buf := bytes.Buffer{}
	A, B, C := 0, 0, 0
	total := a + b + c

	for i := 0; i < total; i++ {
		if (a >= b && a >= c && A < 2) || (a > 0 && (B >= 2 || C >= 2)) {
			buf.WriteByte('a')
			a--
			A, B, C = A+1, 0, 0
		} else if (b >= a && b >= c && B < 2) || (b > 0 && (A >= 2 || C >= 2)) {
			buf.WriteByte('b')
			b--
			A, B, C = 0, B+1, 0
		} else if (c >= a && c >= b && C < 2) || (c > 0 && (A >= 2 || B >= 2)) {
			buf.WriteByte('c')
			c--
			A, B, C = 0, 0, C+1
		} else {
			break
		}
	}

	return buf.String()
}
