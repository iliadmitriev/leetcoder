const (
	Base  = '1'
	Empty = '.'
)

type sudoku []int

func NewSudoku(n int) sudoku {
	return make([]int, n)
}

func (s sudoku) set(v byte) bool {
	if v == Empty {
		return true
	}

	if s[v-Base] >= 1 {
		return false
	}

	s[v-Base]++
	return true
}

func (s sudoku) reset() {
	for i := range s {
		s[i] = 0
	}
}

func isValidSudoku(board [][]byte) bool {
	const (
		N = 9
		M = N + 1
		D = 3
	)

	sud := NewSudoku(M)

	for i := range N {
		sud.reset()

		for j := range N {
			if !sud.set(board[i][j]) {
				return false
			}
		}
	}

	for j := range N {
		sud.reset()

		for i := range N {
			if !sud.set(board[i][j]) {
				return false
			}
		}
	}

	for i := 0; i < N; i += D {
		for j := 0; j < N; j += D {
			sud.reset()

			for r := i; r < i+D; r++ {
				for c := j; c < j+D; c++ {
					if !sud.set(board[r][c]) {
						return false
					}
				}
			}
		}
	}

	return true
}
