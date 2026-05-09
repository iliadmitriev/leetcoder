
func canChange(start string, target string) bool {
	m := len(start)

	for i, j := 0, 0; i < m || j < m; i, j = i+1, j+1 {
		for i < m && start[i] == '_' {
			i++
		}

		for j < m && target[j] == '_' {
			j++
		}

		if i == m || j == m {
			return i == m && j == m
		}

		if start[i] != target[j] {
			return false
		}

		if start[i] == 'L' && i < j {
			return false
		}

		if start[i] == 'R' && i > j {
			return false
		}

	}

	return true
}
