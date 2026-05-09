
func minDeletionSize(strs []string) int {
	rows := len(strs)
	cols := len(strs[0])

	deleted := 0

	for c := range cols {
		for r := 1; r < rows; r++ {
			if strs[r-1][c] > strs[r][c] {
				deleted++
				break
			}
		}
	}

	return deleted
}
