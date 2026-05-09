func numberOfSubmatrices(grid [][]byte) int {

	m, n := len(grid), len(grid[0])
	count := 0
	X, Y := make([]int, n), make([]int, n)

	for i := range m {
    x, y := 0, 0
		for j := range n {
      switch grid[i][j] {
        case 'Y': y++
        case 'X': x++
      }

      X[j] += x
      Y[j] += y

      if X[j] > 0 && X[j] == Y[j] {
        count++
      }
		}
	}

	return count
}