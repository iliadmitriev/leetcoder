func minOperations(logs []string) int {
	path := 0
	for _, log := range logs {
		if log == "../" {
			if path > 0 {
				path--
			}
		} else if log != "./" {
			path++
		}
	}

	return path
}
