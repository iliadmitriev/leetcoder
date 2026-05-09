import "sort"

func distributeCandies(candyType []int) int {
	unique := 1
	sort.Ints(candyType)

	for i := 1; i < len(candyType); i++ {
		if candyType[i] != candyType[i-1] {
			unique++
		}
	}

	return min(len(candyType)/2, unique)
}
