func numRookCaptures(board [][]byte) int {
	rookRow, rookCol := findFigureAtBoard(board, 'R')
	res := 0
	dirs := [][2]int{[2]int{0, 1}, [2]int{1, 0}, [2]int{0, -1}, [2]int{-1, 0}}

	for _, d := range dirs {

		for r, c := rookRow, rookCol; r >= 0 && r < len(board) && c >= 0 && c < len(board[0]) && board[r][c] != 'B'; r, c = r+d[0], c+d[1] {
			if board[r][c] == 'p' {
				res++
				break
			}
		}
	}

	return res
}

func findFigureAtBoard(board [][]byte, figure byte) (int, int) {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] == figure {
				return i, j
			}
		}
	}

	return -1, -1
}
