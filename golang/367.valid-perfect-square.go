func isPerfectSquare(num int) bool {
	x := sqrtNewton(num)

	return x*x == num
}

func sqrtNewton(x int) int {
	y := x

	for y*y > x {
		y = (y + x/y) / 2
	}
	return y
}
