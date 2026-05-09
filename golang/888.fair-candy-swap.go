func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
	totalAlice := 0
	for _, alice := range aliceSizes {
		totalAlice += alice
	}

	totalBob := 0
	bobSet := make(map[int]bool, len(bobSizes))
	for _, bob := range bobSizes {
		totalBob += bob
		bobSet[bob] = true
	}

	draw := (totalAlice + totalBob) / 2
	diff := draw - totalAlice

	for _, alice := range aliceSizes {
		if _, ok := bobSet[diff+alice]; ok {
			return []int{alice, diff + alice}
		}
	}

	return []int{0, 0}
}
