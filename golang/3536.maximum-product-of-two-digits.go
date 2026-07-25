func maxProduct(n int) int {
	var d, d1, d2 int

	for ; n > 0; n /= 10 {
		d = n % 10

		if d >= d1 {
			d2 = d1
			d1 = d
		} else if d > d2 {
			d2 = d
		}
	}

	return d1 * d2
}