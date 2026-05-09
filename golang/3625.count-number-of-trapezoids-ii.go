
func countTrapezoids(points [][]int) int {
	mids := make(map[int][]float64)
	slopes := make(map[float64][]float64)

	INF := math.Inf(1)
	n := len(points)

	for i := range n {
		for j := i + 1; j < n; j++ {
			x1, y1 := points[i][0], points[i][1]
			x2, y2 := points[j][0], points[j][1]

			dx := float64(x1 - x2)
			dy := float64(y1 - y2)

			var k, b float64

			if x1 == x2 {
				k = INF
				b = float64(x1)
			} else {
				k = float64(y2-y1) / float64(x2-x1)
				b = (float64(y1)*dx - float64(x1)*dy) / dx
			}

			mKey := (x1+x2)*10000 + (y1 + y2)
			slopes[k] = append(slopes[k], b)
			mids[mKey] = append(mids[mKey], k)
		}
	}

	ans := 0

	for _, k := range slopes {
		if len(k) < 2 {
			continue
		}

		cnt := make(map[float64]int)
		for _, v := range k {
			cnt[v]++
		}

		total := 0
		for _, v := range cnt {
			ans += total * v
			total += v
		}
	}

	for _, m := range mids {
		if len(m) < 2 {
			continue
		}

		cnt := make(map[float64]int)
		for _, v := range m {
			cnt[v]++
		}

		total := 0
		for _, v := range cnt {
			ans -= total * v
			total += v
		}
	}

	return ans
}
