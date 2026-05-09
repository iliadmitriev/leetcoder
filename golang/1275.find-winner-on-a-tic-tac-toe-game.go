func tictactoe(moves [][]int) string {
	// 3 rows, 3 cols, 2 diagonals (total 8)
	A, B := make([]int, 8), make([]int, 8)

	for i, m := range moves {
		// set pointer on player A or B depending on the turn parity
		r, c := m[0], m[1]

		p := ([]int)(nil)
		if i%2 == 0 {
			p = A
		} else {
			p = B
		}

		p[r]++
		p[3+c]++
		if r == c {
			p[6]++
		}

		if r == 2-c {
			p[7]++
		}
	}

	for j := 0; j < 8; j++ {
		if A[j] == 3 {
			return "A"
		}
		if B[j] == 3 {
			return "B"
		}
	}

	if len(moves) == 9 {
		return "Draw"
	}

	return "Pending"
}
