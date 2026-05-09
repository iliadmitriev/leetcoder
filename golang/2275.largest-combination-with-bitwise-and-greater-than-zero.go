func largestCombination(candidates []int) int {
	bc := make([]int, 24)

	for _, num := range candidates {
		for i := 0; num > 0; i, num = i+1, num>>1 {
			bc[i] += num & 1
		}
	}

	maxBits := bc[0]
	for _, bits := range bc {
		maxBits = max(maxBits, bits)
	}

	return maxBits
}
