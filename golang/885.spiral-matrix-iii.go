
func coordsFitMat(r, c, rows, cols int) bool {
	return 0 <= r && r < rows && 0 <= c && c < cols
}

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	coords := make([][]int, 0, rows*cols)
	r, c := rStart, cStart
	// direction 0-> east, 1-> south, 2-> west, 3-> north
	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	dir := 0
	// cycle: number of cells in one direction
	cycle := 1

	for i := 0; len(coords) < rows*cols; i++ {
		for j := 0; j < cycle; j++ {
			if coordsFitMat(r, c, rows, cols) {
				coords = append(coords, []int{r, c})
			}
			r, c = dirs[dir][0]+r, dirs[dir][1]+c
		}

		dir = (dir + 1) % 4 // change direction every loop iteration
		cycle += i % 2      // increase cycle length every 2 loop iterations
	}

	return coords
}

// direction cycle

// right 1
// down 1
// left 2
// top 2

// right 3
// down 3
// left 4
// top 4
