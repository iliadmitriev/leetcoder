func reverseDegree(s string) int {
	degree := 0
	base := int('a') + 26

	for i, ch := range s {
		degree += (i + 1) * (base - int(ch))
	}

	return degree
}