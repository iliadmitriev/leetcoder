func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
	n := len(bottomLeft)
	maxArea := 0

	for i := range n {
		for j := range n {
			if i == j {
				continue
			}

			x11, y11 := bottomLeft[i][0], bottomLeft[i][1] // 2, 2
			x12, y12 := topRight[i][0], topRight[i][1]     // 4, 4

			x21, y21 := bottomLeft[j][0], bottomLeft[j][1] // 1, 1
			x22, y22 := topRight[j][0], topRight[j][1]     // 3, 3

			x1, x2 := max(x11, x21), min(x12, x22) // 2, 3
			y1, y2 := max(y11, y21), min(y12, y22) // 2, 3

			dx := max(0, x2-x1) // 1
			dy := max(0, y2-y1) // 1

			side := min(dx, dy) // 1

			maxArea = max(maxArea, side*side) // 1
		}
	}

	return int64(maxArea)
}