func numberOfArrays(differences []int, lower int, upper int) int {
	cur, bottom, top := 0, 0, 0
	for _, diff := range differences {
		cur += diff
		bottom, top = min(bottom, cur), max(top, cur)
	}

	delta := upper - lower
	diff := top - bottom

	if delta < diff {
		return 0
	}

	return delta - diff + 1
}
