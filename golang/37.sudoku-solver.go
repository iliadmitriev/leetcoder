
const (
	N     = 9
	ALL   = (1 << (N + 1)) - 1
	EMPTY = '.'
	BASE  = '1'
)

func solveSudoku(board [][]byte) {
	rows := make([]int, N)
	cols := make([]int, N)
	blocks := make([]int, N)
	empties := make([][2]int, 0)

	for i := range N {
		rows[i] = ALL
		cols[i] = ALL
		blocks[i] = ALL
	}

	for i := range N {
		for j := range N {
			if board[i][j] == EMPTY {
				empties = append(empties, [2]int{i, j})
			} else {
				mask := 1 << (board[i][j] - BASE)
				rows[i] ^= mask
				cols[j] ^= mask
				blocks[i/3*3+j/3] ^= mask
			}
		}
	}

	dfsSudoku(board, rows, cols, blocks, empties, 0)
}

func dfsSudoku(board [][]byte, rows, cols, blocks []int, empties [][2]int, i int) bool {
	if i == len(empties) {
		return true
	}

	r, c := empties[i][0], empties[i][1]

	available := rows[r] & cols[c] & blocks[r/3*3+c/3]

	if available == 0 {
		return false
	}

	for j := range N {
		can := 1 << j

		if (available & can) == 0 {
			continue
		}

		rows[r] ^= can
		cols[c] ^= can
		blocks[r/3*3+c/3] ^= can

		board[r][c] = byte(BASE + j)

		if dfsSudoku(board, rows, cols, blocks, empties, i+1) {
			return true
		}

		rows[r] ^= can
		cols[c] ^= can
		blocks[r/3*3+c/3] ^= can
	}

	return false
}
