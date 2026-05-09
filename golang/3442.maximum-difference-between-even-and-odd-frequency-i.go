import "math"

func maxDifference(s string) int {
	cnt := make([]int, 26)
	a1, a2 := 0, math.MaxInt
	for _, c := range s {
		cnt[c-'a']++
	}

	for _, c := range cnt {
		if c == 0 {
			continue
		}

		if c%2 == 1 {
			a1 = max(a1, c)
		} else {
			a2 = min(a2, c)
		}
	}

	return a1 - a2
}
