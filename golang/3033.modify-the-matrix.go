
type ColumnMax struct {
	colMax []int
}

func (cache ColumnMax) GetMaxCol(mat [][]int, col int) int {

	if cache.colMax[col] != -1 {
		return cache.colMax[col]
	}

	m := len(mat)
	for i := 0; i < m; i++ {
		cache.colMax[col] = max(cache.colMax[col], mat[i][col])
	}

	return cache.colMax[col]
}

func NewColumnMax(cols int) ColumnMax {
	colMax := make([]int, cols)
	for i := 0; i < cols; i++ {
		colMax[i] = -1
	}

	return ColumnMax{colMax: colMax}
}

func modifiedMatrix(matrix [][]int) [][]int {
	cache := NewColumnMax(len(matrix[0]))

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == -1 {
				matrix[i][j] = cache.GetMaxCol(matrix, j)
			}
		}
	}

	return matrix
}
