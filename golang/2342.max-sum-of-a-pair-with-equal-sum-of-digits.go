func maximumSum(nums []int) int {
	cache := make(map[int][]int, 0)
	maxSum := -1

	for _, num := range nums {
		key := sumOfDigits(num)
		cache[key] = append(cache[key], num)
	}

	for _, pairs := range cache {
		maxSum = max(maxSum, maxPairSum(pairs))
	}

	return maxSum
}

func sumOfDigits(n int) int {
	s := 0
	for n > 0 {
		s += n % 10
		n /= 10
	}

	return s
}

func maxPairSum(arr []int) int {
	if len(arr) < 2 {
		return -1
	}

	N := len(arr)
	max1, max2 := arr[0], arr[1]
	if max1 < max2 {
		max1, max2 = max2, max1
	}

	for i := 2; i < N; i++ {
		if arr[i] > max1 {
			max1, max2 = arr[i], max1
		} else if arr[i] > max2 {
			max2 = arr[i]
		}
	}

	return max1 + max2
}
