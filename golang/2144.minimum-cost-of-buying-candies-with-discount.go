import (
	"cmp"
	"slices"
)

func minimumCost(cost []int) int {
	total := 0
	slices.SortFunc(cost, func(a, b int) int {
		return cmp.Compare(b, a)
	})

	for i, c := range cost {
		if (i+1)%3 == 0 {
			continue
		}

		total += c
	}

	return total
}