
const MOD int = 1e9 + 7

func numSub(s string) int {
	count := func(n int) int {
		return n * (n + 1) / 2
	}

	total := 0
	cur := 0

	for _, c := range s {
		if c == '1' {
			cur++
		} else {
			total += count(cur)
			total %= MOD
			cur = 0
		}
	}

	total += count(cur)
	total %= MOD

	return total
}
