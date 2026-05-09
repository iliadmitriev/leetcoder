func canCollectBouqetes(bloomDay []int, mid, m, k int) bool {
	j := 0
	for _, bd := range bloomDay {
		if bd <= mid {
			j++
		} else {
			j = 0
		}

		if j == k {
			m--
			j = 0
		}

		if m == 0 {
			break
		}
	}

	return m <= 0
}

func minDays(bloomDay []int, m int, k int) int {
	if len(bloomDay) < m*k {
		return -1
	}

	lo, hi := bloomDay[0], bloomDay[0]
	for _, bd := range bloomDay {
		lo = min(lo, bd)
		hi = max(hi, bd)
	}

	var mid int
	for lo < hi {
		mid = (lo + hi) / 2

		if canCollectBouqetes(bloomDay, mid, m, k) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
