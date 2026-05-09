func removeStones(stones [][]int) int {
	vis := make(map[[2]int]bool)
	components := 0

	adjRow, adjCol := make(map[int][]int), make(map[int][]int)

	for i := 0; i < len(stones); i++ {
		r, c := stones[i][0], stones[i][1]
		adjRow[r] = append(adjRow[r], c)
		adjCol[c] = append(adjCol[c], r)
	}

	for _, e := range stones {
		if vis[[2]int{e[0], e[1]}] {
			continue
		}

		__dfsFindComponents(adjRow, adjCol, vis, e[0], e[1])
		components++
	}

	return len(stones) - components
}

func __dfsFindComponents(adjRow, adjCol map[int][]int, vis map[[2]int]bool, row, col int) {
	vis[[2]int{row, col}] = true

	for _, nextCol := range adjRow[row] {
		if vis[[2]int{row, nextCol}] {
			continue
		}

		__dfsFindComponents(adjRow, adjCol, vis, row, nextCol)
	}

	for _, nextRow := range adjCol[col] {
		if vis[[2]int{nextRow, col}] {
			continue
		}

		__dfsFindComponents(adjRow, adjCol, vis, nextRow, col)
	}
}
