import "math"

func constructRectangle(area int) []int {
	top := int(math.Sqrt(float64(area)))

	for side := top; side >= 1; side-- {
		if area%side == 0 {
			return []int{area / side, side}
		}
	}

	return []int{area, 1}
}
