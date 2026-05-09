func minSum(nums1 []int, nums2 []int) int64 {
	sumA, sumB, zeroA, zeroB := 0, 0, 0, 0
	for _, num := range nums1 {
		if num == 0 {
			zeroA++
		}

		sumA += num
	}

	for _, num := range nums2 {
		if num == 0 {
			zeroB++
		}

		sumB += num
	}

	if zeroA == 0 && sumA < sumB+zeroB {
		return -1
	}

	if zeroB == 0 && sumB < sumA+zeroA {
		return -1
	}

	return int64(max(sumA+zeroA, sumB+zeroB))
}
