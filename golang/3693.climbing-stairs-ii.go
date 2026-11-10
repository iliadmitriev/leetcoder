func climbStairs(n int, costs []int) int {
	f, f1, f2 := 0, 0, 0

	for _, cost := range costs {
		f, f1, f2 = cost+min(f+1, f1+4, f2+9), f, f1
	}

	return f
}