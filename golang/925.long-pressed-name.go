func isLongPressedName(name string, typed string) bool {
	n, t := len(name), len(typed)
	i, j := 0, 0

	for i < n && j < t {
		a, b := name[i], typed[j]

		if a != b {
			return false
		}

		c1, c2 := 0, 0
		for i < n && name[i] == a {
			i++
			c1++
		}

		for j < t && typed[j] == b {
			j++
			c2++
		}

		if c1 > c2 {
			return false
		}
	}

	return i == n && j == t
}
