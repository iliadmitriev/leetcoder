func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	x1, y1, x2, y2 := rec1[0], rec1[1], rec1[2], rec1[3]
	x3, y3, x4, y4 := rec2[0], rec2[1], rec2[2], rec2[3]

	xa, ya := max(x1, x3), max(y1, y3)
	xb, yb := min(x2, x4), min(y2, y4)

	return xa < xb && ya < yb
}
