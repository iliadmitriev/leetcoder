func maximumCandies(candies []int, k int64) int {
	total := makeSum(candies)
	if k > int64(total) {
		return 0
	}

	res := 0
	lo, hi := 1, total/int(k)+1
	var mid int
	for lo < hi {
		mid = (lo + hi) / 2

		if checkMaxCandies(candies, mid, k) {
			res = mid
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return res
}

func makeSum(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}

func checkMaxCandies(candies []int, v int, k int64) bool {
	d := int(k)
	for i := 0; i < len(candies); i++ {
		d -= candies[i] / v
		if d <= 0 {
			return true
		}
	}

	return false
}
