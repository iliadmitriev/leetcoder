func matrixReshape(mat [][]int, r int, c int) [][]int {
	R, C := len(mat), len(mat[0])

	if R == r && C == c {
		return mat
	}

	if R*C != r*c {
		return mat
	}

	res := make([][]int, r)
	for i := range res {
		res[i] = make([]int, c)

		for j := range res[i] {
			res[i][j] = mat[(i*c+j)/C][(i*c+j)%C]
		}
	}

	return res
}
