import "sort"

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
	merge := make(map[int]int, len(items1)+len(items2))

	for i := 0; i < len(items1); i++ {
		merge[items1[i][0]] += items1[i][1]
	}

	for i := 0; i < len(items2); i++ {
		merge[items2[i][0]] += items2[i][1]
	}

	keyList := make([]int, 0, len(merge))
	for k := range merge {
		keyList = append(keyList, k)
	}

	sort.Ints(keyList)

	res := make([][]int, 0, len(merge))
	for _, k := range keyList {
		res = append(res, []int{k, merge[k]})
	}

	return res
}
