
func projectionArea(grid [][]int) int {
	xy, yz, zx := 0, 0, 0

	n := len(grid)

	for i := 0; i < n; i++ {
		z1, z2 := 0, 0
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				xy++
			}
			z1 = max(z1, grid[i][j])
			z2 = max(z2, grid[j][i])
		}

		yz += z1
		zx += z2
	}

	return xy + yz + zx
}
