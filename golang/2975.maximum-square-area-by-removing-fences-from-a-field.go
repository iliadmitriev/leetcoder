func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
	const MOD = int(1e9) + 7

	hFences = append(hFences, 1, m)
	vFences = append(vFences, 1, n)

	sort.Ints(hFences)
	sort.Ints(vFences)

	area := 0
	hCache := map[int]bool{}

	for i := 1; i < len(hFences); i++ {
		for j := 0; j < i; j++ {
			hCache[hFences[i]-hFences[j]] = true
		}
	}

	for i := 1; i < len(vFences); i++ {
		for j := 0; j < i; j++ {
			w := vFences[i] - vFences[j]
			if hCache[w] {
				area = max(area, w*w)
			}
		}
	}

	if area == 0 {
		return -1
	}

	return area % MOD
}