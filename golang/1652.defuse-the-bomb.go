func decrypt(code []int, k int) []int {

	n := len(code)
	res := make([]int, n)

	if k == 0 {
		return res
	}

	left, right := 1, 1+k

	if k < 0 {
		left, right = n+k, n
	}

	window := 0
	for i := left; i < right; i++ {
		window += code[i]
	}

	for i := 0; i < n; i++ {
		res[i] = window
		window -= code[(i+left)%n]
		window += code[(i+right)%n]
	}

	return res
}
