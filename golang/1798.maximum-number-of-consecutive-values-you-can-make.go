import "sort"

func getMaximumConsecutive(coins []int) int {
	cover := 1
	sort.Ints(coins)

	for _, coin := range coins {
		if coin > cover {
			break
		}

		cover += coin
	}

	return cover
}
