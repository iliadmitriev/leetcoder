func maxDistance(colors []int) int {
	n := len(colors)
	left, right := 0, n-1

	for left < n && colors[left] == colors[n-1] {
		left++
	}

	for right >= 0 && colors[right] == colors[0] {
		right--
	}

	return max(right, n-left-1)
}
