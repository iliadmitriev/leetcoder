func snakesAndLadders(board [][]int) int {
	m, n := len(board), len(board[0])
	start, finish := 1, m*n
	size := finish + 1

	b := make([]int, size)       // board (flaten)
	v := make([]bool, size)      // visited
	q := make([][2]int, 0, size) // queue of {node, moves}

	// left to right
	ltr := true
	// build flaten, lined up board
	for i, r := 1, m-1; r >= 0; r-- {
		for j := range n {
			c := j
			if !ltr {
				c = n - 1 - j
			}

			b[i] = board[r][c]
			i++
		}

		ltr = !ltr
	}

	// start bfs
	q = append(q, [2]int{start, 0})
	v[start] = true

	for len(q) > 0 {
		node, moves := q[0][0], q[0][1]
		q = q[1:]

		if node == finish {
			return moves
		}

		for dice := 6; dice >= 1; dice-- { // roll the dice
			dest := min(node+dice, finish)

			// snake or ladder
			if b[dest] != -1 {
				dest = b[dest]
			}

			if !v[dest] {
				v[dest] = true
				q = append(q, [2]int{dest, moves + 1})
			}
		}
	}

	return -1
}
