func pushDominoes(dominoes string) string {
	type item struct {
		i int
		d byte
	}

	dom := []byte(dominoes)
	n := len(dom)
	q := make([]item, 0, n)

	for i := range n {
		if dom[i] == 'L' || dom[i] == 'R' {
			q = append(q, item{i, dom[i]})
		}
	}

	for len(q) > 0 {
		i, d := q[0].i, q[0].d
		q = q[1:]

		if d == 'L' && i > 0 && dom[i-1] == '.' {
			dom[i-1] = 'L'
			q = append(q, item{i - 1, 'L'})
		} else if d == 'R' && i+1 < n && dom[i+1] == '.' {
			if i+2 < n && dom[i+2] == 'L' {
				q = q[1:]
			} else {
				dom[i+1] = 'R'
				q = append(q, item{i + 1, 'R'})
			}
		}
	}

	return string(dom)
}
