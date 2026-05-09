/*
p - prime number
mod - big prime number
     head       tail
x = [0,1,2,3,...n]

h(x) = ( x(0) * p^(n) + x(1) * p^(n - 1) ... * x(n) * p(0) ) % mod
h(x) = ( ( ( x(0) * p % mod ) * p + x(1) ) % mod ... ) +  x(n) ) % mod

// add to tail
h(x) = ( h(x(n-1)) * p + x(n) ) % mod

// remove from head
h(x(n-1)) = ( mod + h(x) - x(0) * p^(n) % mod ) % mod
*/
func strStr(haystack string, needle string) int {

	m, n := len(haystack), len(needle)
	if n > m {
		return -1
	}

	const (
		MOD = int(1e9) + 7
		P   = int(29)
	)

	// modular exponent MOD
	exp := func(base, e int) int {
		res := 1

		for e > 0 {
			if e&1 == 1 {
				res = (res * base) % MOD
			}
			base = (base * base) % MOD
			e >>= 1
		}

		return res
	}

	P_n := exp(P, n)

	// add to tail symbol x
	add := func(hash int, x byte) int {
		return (hash*P + int(x)) % MOD
	}

	// discard from head symbol x (n-th from tail)
	discard := func(hash int, x byte) int {
		return (MOD + hash - int(x)*P_n % MOD) % MOD
	}

	p := 0 // pattern to search for
	h := 0 // current rolling hash

	for i := range n {
		p = add(p, needle[i])
		h = add(h, haystack[i])
	}

	if h == p && needle == haystack[:n] {
		return 0
	}

	for i := n; i < m; i++ {
		h = add(h, haystack[i])
		h = discard(h, haystack[i-n])

		if h == p && needle == haystack[i-n+1:i+1] {
			return i - n + 1
		}
	}

	return -1
}