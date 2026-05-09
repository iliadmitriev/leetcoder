func minimizedMaximum(n int, quantities []int) int {
	maxBucket := 0

	total := summarize(quantities)
	lo, hi := max(1, total/n), total+1
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if checkDistribution(n, quantities, mid) {
			hi = mid
			maxBucket = mid
		} else {
			lo = mid + 1
		}
	}

	return maxBucket
}

func summarize(arr []int) int {
	res := 0
	for _, v := range arr {
		res += v
	}
	return res
}

func checkDistribution(n int, quantities []int, mid int) bool {
	for _, q := range quantities {
		n -= q / mid
		if q%mid > 0 {
			n--
		}

		if n < 0 {
			return false
		}
	}
	return true
}
