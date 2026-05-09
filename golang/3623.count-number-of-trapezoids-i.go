
func countTrapezoids(points [][]int) int {
	const MOD = int(1e9) + 7
	cnt := make(map[int]int, len(points))
	for _, p := range points {
		cnt[p[1]]++
	}

	var res, total int

	for _, v := range cnt {
		edges := v * (v - 1) / 2

		res += total * edges
		res %= MOD

		total += edges
		total %= MOD
	}

	return res
}
