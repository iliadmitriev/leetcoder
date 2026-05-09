func tupleSameProduct(nums []int) int {
	N := len(nums)
	res := 0
	pairs := make(map[int]int)

	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			pairs[nums[i]*nums[j]]++
		}
	}

	for _, v := range pairs {
		res += v * (v - 1)
	}

	return res * 4
}
