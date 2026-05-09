func findRotation(mat [][]int, target [][]int) bool {
	eq := func(mat1, mat2 [][]int) bool {
		m, n := len(mat1), len(mat1[0])

		if m != len(mat2) || n != len(mat2[0]) {
			return false
		}

		for i := range m {
			for j := range n {
				if mat1[i][j] != mat2[i][j] {
					return false
				}
			}
		}

		return true
	}

	rot90 := func(mat [][]int) {
		n := len(mat) // no width, width == height

		var tmp int

		for i := range n/2 + n%2 {
			for j := range n / 2 {
				tmp = mat[i][j]                   // save top left
				mat[i][j] = mat[n-1-j][i]         // move bottom left to top left
				mat[n-1-j][i] = mat[n-1-i][n-1-j] // move bottom right to bottom left
				mat[n-1-i][n-1-j] = mat[j][n-1-i] // move top right to bottom right
				mat[j][n-1-i] = tmp               // saved value (ex top left) to bottom left
			}
		}
	}

	if eq(mat, target) {
		return true
	}

	for range 3 {
		rot90(mat)
		if eq(mat, target) {
			return true
		}
	}

	return false
}