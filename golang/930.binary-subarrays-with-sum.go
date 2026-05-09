func numSubarraysWithSum(nums []int, goal int) int {
	cursSum := 0
	prefixSums := map[int]int{0: 1}
	res := 0

	for _, num := range nums {
		cursSum += num
		res += prefixSums[cursSum-goal]
		prefixSums[cursSum]++
	}

	return res
}
