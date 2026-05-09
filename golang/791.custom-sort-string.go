func customSortString(order string, s string) string {
	c := make(map[rune]int, 26)
	for _, v := range s {
		c[v]++
	}

	res := make([]rune, 0, len(s))
	for _, o := range order {
		if c[o] == 0 {
			continue
		}

		for v := c[o]; v > 0; v-- {
			res = append(res, o)
		}

		delete(c, o)
	}

	for k, v := range c {
		for ; v > 0; v-- {
			res = append(res, k)
		}
	}

	return string(res)
}
