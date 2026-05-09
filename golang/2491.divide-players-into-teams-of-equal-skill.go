func dividePlayers(skill []int) int64 {
	total := 0
	for _, v := range skill {
		total += v
	}

	pairs := len(skill) / 2

	if total%pairs != 0 {
		return -1
	}

	target := total / pairs

	skillSet := make(map[int]int)
	for _, v := range skill {
		skillSet[v]++
	}

	if target%2 == 0 && skillSet[target/2]%2 != 0 {
		return -1
	} else if target%2 == 0 {
		skillSet[target/2] /= 2
	}

	chemistry := 0
	for k, v := range skillSet {
		if skillSet[target-k] != v {
			return -1
		}

		chemistry += k * (target - k) * v
		skillSet[target-k] = 0
		skillSet[k] = 0
	}

	return int64(chemistry)
}
