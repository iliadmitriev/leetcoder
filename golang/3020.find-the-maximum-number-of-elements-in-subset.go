func maximumLength(nums []int) int {
	cnt := make(map[int]int) // K -> V, K = [1,N], V = [1,M], N = len(nums), M = max(nums)
	for _, num := range nums {
		cnt[num]++
	}

	res := 0

	// count 1's separately
	if ones, ok := cnt[1]; ok {
		// max odd number greater or equal to ones
		res = max(res, ones-1+(ones&1))

		delete(cnt, 1) // delete 1's
	}

	for key, _ := range cnt {
		length := 0
		k := key

		for ; cnt[k] > 1; k *= k {
			length += 2
		}

		if _, ok := cnt[k]; ok {
			res = max(res, length+1)
		} else {
			res = max(res, length-1)
		}
	}

	return res
}