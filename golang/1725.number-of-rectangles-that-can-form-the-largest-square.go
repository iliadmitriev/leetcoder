func countGoodRectangles(rectangles [][]int) int {
	maxSquare, countSquares := 0, 0

	for _, rect := range rectangles {
		if square := min(rect[0], rect[1]); square > maxSquare {
			maxSquare = square
			countSquares = 1
		} else if square == maxSquare {
			countSquares++
		}
	}

	return countSquares
}
