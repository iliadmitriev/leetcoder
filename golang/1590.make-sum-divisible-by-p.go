func minSubarray(nums []int, p int) int {
	total := 0
	for _, v := range nums {
		total += v
	}

	remain := total % p
	if remain == 0 {
		return 0
	}

	if total < p {
		return -1
	}

	remainders := make(map[int]int)
	remainders[0] = -1
	curSum := 0
	prefix := 0
	minLen := len(nums)

	for i, num := range nums {
		curSum = (curSum + num) % p
		prefix = (curSum + p - remain) % p

		if j, ok := remainders[prefix]; ok {
			minLen = min(minLen, i-j)
		}

		remainders[curSum] = i
	}

	if minLen == len(nums) {
		return -1
	}

	return minLen
}
