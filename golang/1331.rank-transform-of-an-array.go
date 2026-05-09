import "sort"

func arrayRankTransform(arr []int) []int {

	nums := make([]int, len(arr))
	copy(nums, arr)

	sort.Ints(nums)

	ranks := make(map[int]int, len(nums))
	rank := 1

	for _, num := range nums {
		if _, ok := ranks[num]; !ok {
			ranks[num] = rank
			rank++
		}
	}

	for i := range arr {
		arr[i] = ranks[arr[i]]
	}

	return arr
}
