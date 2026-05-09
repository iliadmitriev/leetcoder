func minCost(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])


	points := make([][2]int, 0, m*n) // list of points sorted by their weight in grid matrix ascending

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			points = append(points, [2]int{i, j})
		}
	}

	sort.Slice(points, func(i, j int) bool {
		return grid[points[i][0]][points[i][1]] < grid[points[j][0]][points[j][1]]
	})

	costs := make([][]int, m)

	for i := range costs {
		costs[i] = make([]int, n)
		for j := range costs[i] {
			costs[i][j] = math.MaxInt
		}
	}

	for range k + 1 {
		minCost := math.MaxInt

		for i, j := 0, 0; i < len(points); i++ {
			minCost = min(minCost, costs[points[i][0]][points[i][1]])

			if i+1 < len(points) && grid[points[i][0]][points[i][1]] == grid[points[i+1][0]][points[i+1][1]] {
				continue
			}

			for r := j; r <= i; r++ {
				costs[points[r][0]][points[r][1]] = minCost
			}

			j = i + 1
		}

		for i := m - 1; i >= 0; i-- {
			for j := n - 1; j >= 0; j-- {
				if i == m-1 && j == n-1 {
					costs[i][j] = 0
					continue
				}

				if i != m-1 {
					costs[i][j] = min(costs[i][j], costs[i+1][j]+grid[i+1][j])
				}

				if j != n-1 {
					costs[i][j] = min(costs[i][j], costs[i][j+1]+grid[i][j+1])
				}
			}
		}
	}

	return costs[0][0]
}