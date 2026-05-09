
func isArrangable(position []int, m int, d int) bool {
	m--
	i := 0

	for j := 1; j < len(position); j++ {
		if position[j]-position[i] >= d {
			m--
			i = j
		}

		if m <= 0 {
			break
		}
	}

	return m <= 0
}

func maxDistance(position []int, m int) int {
	sort.Ints(position)
	// optimize 1
	if m == 2 {
		return position[len(position)-1] - position[0]
	}

	lo, hi := 1, (position[len(position)-1]-position[0])/(m-1)
	var mid int
	for lo < hi {
		mid = (lo + hi + 1) / 2

		if isArrangable(position, m, mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}

	return lo
}
