func shiftingLetters(s string, shifts [][]int) string {
	N := len(s)
	base := 26
	bias := int('a')
	st := []byte(s)
	prefix := make([]int, N+1)

	for _, sh := range shifts {
		dir, start, end := 2*sh[2]-1, sh[0], sh[1]+1

		prefix[start] += dir
		prefix[end] -= dir
	}

	cur := 0
	for i := 0; i < N; i++ {
		cur += prefix[i]
		cur %= base

		st[i] = byte(bias + (int(st[i])-bias+cur+base)%base)
	}

	return string(st)
}
