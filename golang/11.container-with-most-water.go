func maxArea(height []int) int {
	area := 0

	for i, j := 0, len(height)-1; i < j; {
		w := j - i
		h := min(height[i], height[j])
		area = max(area, h*w)

		if height[i] < height[j] {
			i++
		} else {
			j--
		}
	}

	return area
}