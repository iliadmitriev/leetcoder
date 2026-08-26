func shortestBeautifulSubstring(s string, k int) string {
	n := len(s)
	i, j := 0, 0
	best := n + 1
	cur := 0

	for l, r := 0, 0; r < n; r++ {
		if s[r] == '1' {
			cur++
		}

		for (l < r && s[l] == '0') || cur > k {
			if s[l] == '1' {
				cur--
			}
			l++
		}

		if cur != k {
			continue
		}

		// ****** cur == k *********

		if r+1-l < best {
			i, j = l, r+1
			best = r + 1 - l
		} else if r+1-l == best && strncmp(s[l:r+1], s[i:j]) < 0 {
			i, j = l, r+1
		}
	}

	return s[i: j]
}

func strncmp(s1, s2 string) int {
  l1, l2 := len(s1), len(s2)
  n := min(l1, l2)

  for i := range n {
    if s1[i] < s2[i] {
      return -1
    } else if s1[i] > s2[i] {
      return 1
    }
  }

  return 0
}