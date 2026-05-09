func removeOccurrences(s string, part string) string {
	N := len(part)
	st := make([]rune, 0, len(s))
	pp := []rune(part)

	for _, ch := range s {
		st = append(st, ch)

		if len(st) < N {
			continue
		}

		i := len(st) - N
		j := 0

		for j < N && st[i] == pp[j] {
			i++
			j++
		}

		if j == N {
			st = st[:len(st)-N]
		}

	}

	return string(st)
}
