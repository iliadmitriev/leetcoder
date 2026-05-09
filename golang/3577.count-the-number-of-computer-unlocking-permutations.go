
func countPermutations(complexity []int) int {
	lowest := complexity[0]
	n := len(complexity)

	for i := 1; i < n; i++ {
		if complexity[i] <= lowest {
			return 0
		}
	}

	const MOD = int(1e9) + 7
	perm := 1

	for i := 2; i < n; i++ {
		perm = perm * i % MOD
	}

	return perm
}
