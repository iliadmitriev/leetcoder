
func toIntDirection(c byte) int {
	switch c {
	case 'L':
		return -1
	case 'R':
		return 1
	default:
		return 0
	}
}

func countCollisions(directions string) int {
	n := len(directions)
	st := make([]int, 0, n)
	collisions := 0

	for i := range n {
		dd := toIntDirection(directions[i])

		for len(st) > 0 && st[len(st)-1] > dd {
			collisions += st[len(st)-1] - dd
			dd = 0
			st = st[:len(st)-1]
		}

		st = append(st, dd)
	}

	return collisions
}
