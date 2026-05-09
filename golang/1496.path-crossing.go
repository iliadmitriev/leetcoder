func isPathCrossing(path string) bool {
	visited := make(map[[2]int]bool, len(path))
	coords := [2]int{0, 0}

  visited[coords] = true

	for _, ort := range path {
		switch ort {
		case 'N': coords[1]++
		case 'S': coords[1]--
		case 'W': coords[0]--
		case 'E': coords[0]++
		}

		if visited[coords] {
			return true
		}

    visited[coords] = true
	}

	return false
}