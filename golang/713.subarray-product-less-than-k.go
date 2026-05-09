func numSubarrayProductLessThanK(nums []int, k int) int {
	res := 0
	prod := 1

	for p, q := 0, 0; q < len(nums); q++ {

		prod *= nums[q]

		for p <= q && prod >= k {
			prod /= nums[p]
			p++
		}

		res += q - p + 1
	}

	return res
}
