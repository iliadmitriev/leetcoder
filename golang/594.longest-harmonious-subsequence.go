
func findLHS(nums []int) int {
	res := 0
	freq := make(map[int]int, len(nums))

	for _, num := range nums {
		freq[num]++
	}

	for k, v := range freq {
		if v2, ok := freq[k+1]; ok {
			res = max(res, v+v2)
		}
	}

	return res
}
