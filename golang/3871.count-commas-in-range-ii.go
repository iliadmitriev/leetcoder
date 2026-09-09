func countCommas(n int64) int64 {
	var (
		exp  int64 = 1000       // current exponent
		nexp int64 = exp * 1000 // next exponent
		p    int64 = 1          // power
		res  int64 = 0
	)

	for exp <= n {
		nexp = min(n+1, exp*1000)

		res += (nexp - exp) * p

		exp = nexp
		p++
	}

	return res
}