func minVal64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func maximumValueSum(nums []int, k int, edges [][]int) int64 {
	var base int64 = 0
	var totalIncreaseDelta int64 = 0
	var numIncreases int64 = 0
	var numDecreases int64 = 0
	var minIncreaseDelta int64 = math.MaxInt64
	var minDecreaseDelta int64 = math.MaxInt64

	k64 := int64(k)

	for _, num := range nums {
		num64 := int64(num)
		XorNum64 := num64 ^ k64
		base += num64

		if XorNum64 > num64 {
			numIncreases++
			totalIncreaseDelta += XorNum64 - num64
			minIncreaseDelta = minVal64(minIncreaseDelta, XorNum64-num64)
		} else {
			numDecreases++
			minDecreaseDelta = minVal64(minDecreaseDelta, num64-XorNum64)
		}
	}

	if numIncreases == 0 {
		return base
	}

	if numIncreases%2 == 0 {
		return base + totalIncreaseDelta
	}

	if numDecreases == 0 {
		return base + totalIncreaseDelta - minIncreaseDelta
	}

	return base + totalIncreaseDelta - minVal64(minIncreaseDelta, minDecreaseDelta)
}
