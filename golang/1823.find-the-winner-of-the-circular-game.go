func findTheWinner(n int, k int) int {
	return find(n, k) + 1
}

func find(n, k int) int {
	if n == 1 {
		return 0
	}

	return (find(n-1, k) + k) % n
}
