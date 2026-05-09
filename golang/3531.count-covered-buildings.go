
import (
	"sort"
)

func countCoveredBuildings(n int, buildings [][]int) int {
	covered := 0
	hor := make(map[int][]int)
	ver := make(map[int][]int)

	for _, b := range buildings {
		x, y := b[0], b[1]

		hor[x] = append(hor[x], y)
		ver[y] = append(ver[y], x)
	}

	for _, ys := range hor {
		sort.Ints(ys)
	}

	for _, xs := range ver {
		sort.Ints(xs)
	}

	for x, ys := range hor {
		for i := 1; i < len(ys)-1; i++ {
			y := ys[i]

			if ver[y][0] < x && x < ver[y][len(ver[y])-1] {
				covered++
			}
		}
	}

	return covered
}
