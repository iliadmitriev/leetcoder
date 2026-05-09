func repairCars(ranks []int, cars int) int64 {
	maxRank := getMaxElement(ranks)
	m := len(ranks)

	lo, hi := 0, maxRank*(cars/m+1)*(cars/m+1)

	for mid := (lo + hi) / 2; lo < hi; mid = (lo + hi) / 2 {
		if isTimeEnoughToRepairCars(ranks, cars, mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return int64(lo)
}

func getMaxElement(arr []int) int {
	m := arr[0]
	for _, v := range arr {
		if v > m {
			m = v
		}
	}
	return m
}

func isTimeEnoughToRepairCars(ranks []int, cars int, t int) bool {
	for _, rank := range ranks {
		cars -= int(math.Sqrt(float64(t / rank)))
		if cars <= 0 {
			return true
		}
	}
	return false
}
