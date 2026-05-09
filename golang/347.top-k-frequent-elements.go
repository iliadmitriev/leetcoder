func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int, len(nums))

	for _, num := range nums {
		freq[num]++
	}

	inv := make(map[int][]int, len(freq))
	for num, f := range freq {
		inv[f] = append(inv[f], num)
	}

	keys := make([]int, 0, len(inv))
	for key := range inv {
		keys = append(keys, key)
	}

	sort.Ints(keys)

	res := make([]int, 0, k)
	for i := len(keys) - 1; k > 0; i-- {
		nn := inv[keys[i]]
		l := min(len(nn), k)
		res = append(res, nn[:l]...)
		k -= l
	}

	return res
}