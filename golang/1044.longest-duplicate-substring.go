func ch2int(c byte) int {
	return int(c-'a') + 1
}

func powMod(base, exp, mod int) int {
	base %= mod
	result := 1
	for exp > 0 {

		if exp&1 > 0 {
			result = (result * base) % mod
		}

		base = (base * base) % mod
		exp >>= 1
	}

	return result
}

func rabinKarp(s string, maxLen int) string {
	if maxLen == 0 {
		return ""
	}

	const mod = int(1e9 + 7)
	const base = 29
	upperLeft := powMod(base, maxLen-1, mod)

	prefix := 0
	for i := 0; i < maxLen; i++ {
		prefix = (prefix*base + ch2int(s[i])) % mod
	}

	seen := make(map[int][]int)
	seen[prefix] = append(seen[prefix], 0)

	for i := 0; i < len(s)-maxLen; i++ {
		prefix = (mod*base + prefix - ch2int(s[i])*upperLeft) % mod
		prefix = (prefix*base + ch2int(s[i+maxLen])) % mod

		if candidates, ok := seen[prefix]; ok {
			for _, j := range candidates {
				if s[i+1:i+1+maxLen] == s[j:j+maxLen] {
					return s[i+1 : i+1+maxLen]
				}
			}
		}

		seen[prefix] = append(seen[prefix], i+1)
	}

	return ""
}

func longestDupSubstring(s string) string {

	lo, hi := 1, len(s)
	var mid int
	var res string

	for lo < hi {
		mid = (lo + hi) / 2

		candidate := rabinKarp(s, mid)

		if len(candidate) > 0 {
			res = candidate
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return res
}

