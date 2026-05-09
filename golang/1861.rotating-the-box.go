const (
	EMPTY    = '.'
	STONE    = '#'
	OBSTACLE = '*'
)

func rotateTheBox(box [][]byte) [][]byte {
	m, n := len(box), len(box[0])
	rotated := make([][]byte, n)
	for j := 0; j < n; j++ {
		rotated[j] = make([]byte, m)
		for i := 0; i < m; i++ {
			rotated[j][i] = EMPTY
		}
	}

	for i := 0; i < m; i++ {
		for j, k := n-1, n-1; j >= 0; j-- {
			if box[i][j] == STONE {
				rotated[k][m-i-1] = STONE
				k--
			} else if box[i][j] == OBSTACLE {
				k = j
				rotated[k][m-i-1] = OBSTACLE
				k--
			}
		}
	}

	return rotated
}
