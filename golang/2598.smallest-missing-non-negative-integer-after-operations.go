func findSmallestInteger(nums []int, value int) int {
	freq := make([]int, value)

	for _, num := range nums {
		num %= value
		if num < 0 {
			num += value
		}

		freq[num]++
	}

	minNum := freq[0]
	minIdx := 0

	for i := 1; i < value && minNum != 0; i++ {
		if freq[i] < minNum {
			minNum = freq[i]
			minIdx = i
		}
	}

	return value*minNum + minIdx
}
