package main

type Code struct {
	Comb string
	Dist int
}

func openLock(deadends []string, target string) int {
	vis := make(map[string]bool, len(deadends))
	for _, d := range deadends {
		vis[d] = true
	}

	if vis["0000"] || vis[target] {
		return -1
	}

	q := make([]Code, 0, 100)
	q = append(q, Code{"0000", 0})
	vis["0000"] = true

	var c Code

	for len(q) > 0 {
		c, q = q[0], q[1:]

		if c.Comb == target {
			return c.Dist
		}

		for i := 0; i < 4; i++ {
			for d := -1; d <= 1; d += 2 {
				next := []rune(c.Comb)
				next[i] = '0' + (10+next[i]-'0'+rune(d))%10
				r := string(next)

				if !vis[r] {
					q = append(q, Code{r, c.Dist + 1})
					vis[r] = true
				}
			}
		}
	}

	return -1
}
