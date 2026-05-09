import "slices"

const BASE = '0'

func findLexSmallestString(s string, a int, b int) string {
	gcd := func(a, b uint8) uint8 {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	// compare two strings or equal length
	less := func(a, b []byte) bool {
		for i := range len(a) {
			if a[i] != b[i] {
				return a[i] < b[i]
			}
		}

		return false
	}

	n := uint8(len(s))       // chain of digits length
	rot := gcd(uint8(b), n)  // rotation step for chain of digits
	rev := gcd(uint8(a), 10) // rotation step for a single digit

	v := []byte(s)
	res := []byte(s)

	// rotate all even or odd digits by `rev` and make t lexicographically smallest
	// i - parity (0 or 1)
	rotate := func(t []byte, i uint8) []byte {
		d := t[i] - BASE
		// d % rev is a minimal possible digit achievable with rotation (revolution) step `rev`
		inc := (10 + d%rev - d) % 10

		if inc == 0 {
			return t
		}

		for j := i; j < n; j += 2 {
			t[j] = ((t[j]-BASE)+inc)%10 + BASE
		}

		return t
	}

	for i := uint8(0); i < n; i += rot {
		t := slices.Concat(v[i:], v[:i])

		t = rotate(t, 1)

		if rot%2 == 1 {
			t = rotate(t, 0)
		}

		if less(t, res) {
			res = t
		}
	}

	return string(res)
}
