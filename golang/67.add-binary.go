func addBinary(a string, b string) string {
	const (
		Base = byte('0')
	)

	m, n := len(a), len(b)
	p := max(m, n) + 1

	c := make([]byte, p)
	carry := byte(0)

	i, j := m-1, n-1
	k := p - 1

	for i >= 0 || j >= 0 || carry > 0 {

		if i >= 0 {
			carry += a[i] ^ Base
		}

		if j >= 0 {
			carry += b[j] ^ Base
		}

		c[k] = carry & 1 ^ Base
		carry >>= 1

		k--
		j--
		i--
	}

	return string(c[k+1:])
}