import "math"

func largestTriangleArea(points [][]int) float64 {
	n := len(points)
	curArea, maxArea := 0.0, 0.0

	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				curArea = triangleArea(points[i], points[j], points[k])
				maxArea = math.Max(maxArea, curArea)
			}
		}
	}

	return maxArea
}

func triangleArea(p1, p2, p3 []int) float64 {
	x1, y1 := float64(p1[0]), float64(p1[1])
	x2, y2 := float64(p2[0]), float64(p2[1])
	x3, y3 := float64(p3[0]), float64(p3[1])

	return math.Abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)) / 2
}
