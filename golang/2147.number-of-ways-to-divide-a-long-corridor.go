
func numberOfWays(corridor string) int {
	const (
		MOD   = int(1e9 + 7)
		SEAT  = 'S'
		PLANT = 'P'
	)

	seats := 0
	div := 1
	total := 1

	for _, cur := range corridor {
		if seats == 2 {
			if cur == PLANT {
				div++
			} else {
				total = total * div % MOD
				seats = 1
				div = 1
			}
		} else {
			if cur == SEAT {
				seats++
			}
		}
	}

	if seats != 2 {
		return 0
	}

	return total
}
