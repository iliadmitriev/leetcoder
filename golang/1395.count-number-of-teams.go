func numTeams(rating []int) int {
	// ascending and descending:
	// number of sequences count for [index, len]
	asc := make([][4]int, len(rating))
	desc := make([][4]int, len(rating))

	// base: all numbers are the sequences of length 1 themselves
	for i := 0; i < len(rating); i++ {
		asc[i][1] = 1
		desc[i][1] = 1
	}

	// counts 2 and 3
	for count := 2; count <= 3; count++ {
		for i := 0; i < len(rating); i++ {
			for j := i + 1; j < len(rating); j++ {
				if rating[i] < rating[j] {
					asc[i][count] += asc[j][count-1]
				} else if rating[i] > rating[j] {
					desc[i][count] += desc[j][count-1]
				}
			}
		}
	}

	res := 0

	for i := 0; i < len(rating); i++ {
		res += asc[i][3] + desc[i][3]
	}

	return res
}
