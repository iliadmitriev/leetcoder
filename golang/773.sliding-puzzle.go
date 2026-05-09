func slidingPuzzle(board [][]int) int {
	moves := [][]byte{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}}
	finish := string([]byte{1, 2, 3, 4, 5, 0, 5})

	vis := make(map[string]bool)
	k := make([]byte, 7) // first row (3) + secod row (3) + zero position (1)

	for i := byte(0); i < 6; i++ {
		k[i] = byte(board[i/3][i%3])

		if k[i] == 0 {
			k[6] = i
		}
	}

	key := string(k)
	vis[key] = true
	q1 := make([]string, 0)

	q1 = append(q1, key)

	for step := 0; len(q1) > 0; step++ {
		for sz := len(q1); sz > 0; sz-- {
			state := q1[0]
			pos := state[6]
			q1 = q1[1:]

			if state == finish {
				return step
			}

			for _, move := range moves[pos] {
				next := []byte(state)
				next[pos], next[move] = next[move], next[pos]
				next[6] = move

				key := string(next)
				if _, ok := vis[key]; ok {
					continue
				}

				vis[key] = true
				q1 = append(q1, key)

			}

		}
	}

	return -1
}
