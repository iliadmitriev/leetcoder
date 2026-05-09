func oddCells(m int, n int, indices [][]int) int {
	rows := make([]int, m)
	cols := make([]int, n)

	for _, i := range indices {
		rows[i[0]] ^= 1
		cols[i[1]] ^= 1
	}

	rowOdd, rowEven, colOdd, colEven := 0, 0, 0, 0
	for _, r := range rows {
		rowOdd += r
		rowEven += 1 - r
	}

	for _, c := range cols {
		colOdd += c
		colEven += 1 - c
	}

	return rowOdd*colEven + rowEven*colOdd
}
