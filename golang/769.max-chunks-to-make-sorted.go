func maxChunksToSorted(arr []int) int {
	chunks := 0
	curMax := -1

	for i, num := range arr {
		curMax = max(curMax, num)
		if curMax == i {
			chunks++
		}
	}

	return chunks
}
