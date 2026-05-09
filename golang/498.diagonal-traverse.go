func findDiagonalOrder(mat [][]int) []int {
	m, n := len(mat), len(mat[0])
	res := make([]int, 0, m*n)
	// key observations:
	// 1. if sum of indices is even, then moving diagonally up-right,
	// and sum parity remains the same until reached the top or right boundary
	// 2. if sum of indices is odd, then moving diagonally down-left,
	// and sum parity remains the same until reached the bottom or left boundary
	i, j := 0, 0

	for range m * n {
		res = append(res, mat[i][j])

		if (i+j)%2 == 0 { // if moving diagonally up-right
			if j == n-1 { // hit the right boundary
				i++ // move down to the next row
			} else if i == 0 { // hit the top boundary
				j++ // move right to the next column
			} else {
				i-- // move up
				j++ // move right
			}
		} else { // if moving diagonally down-left
			if i == m-1 { // and hit the bottom boundary
				j++ // move right to the next column
			} else if j == 0 {
				i++ // move down to the next row
			} else {
				i++ // move down
				j-- // move left
			}
		}
	}

	return res
}
