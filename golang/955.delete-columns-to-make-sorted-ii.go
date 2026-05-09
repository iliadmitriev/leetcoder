
func minDeletionSize(strs []string) int {
	rows := len(strs)
	cols := len(strs[0])

	removed := 0

	inOrder := make([]bool, rows)

	for c := range cols {

		broken := false

		for r := 1; r < rows; r++ {
			if inOrder[r] {
				continue
			}

			if strs[r-1][c] > strs[r][c] {
				broken = true
				break
			}
		}

		if broken {
			removed++
			continue
		}

		for r := 1; r < rows; r++ {
			if !inOrder[r] && strs[r-1][c] < strs[r][c] {
				inOrder[r] = true
			}
		}
	}

	return removed
}
