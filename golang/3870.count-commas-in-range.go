func countCommas(n int) int {
	e := 1000
	p := 1
	res := 0

	for e <= n {
		ne := min(n+1, e*1000)

		res += (ne - e) * p

		e = ne
		p++
	}

	return res
}