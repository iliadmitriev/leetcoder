// example: [1,2,3,4,-5,1,2,4,-4,-3,-2,0,3,1]
// 1,2,3,4
// -5
// 1,2,3,4
// -5,-4,-3,-2,0,3
// -5,-4,-3,-2,0,1
func lengthOfLIS(nums []int) int {
	n := len(nums)
	maxLis := 1
	dp := make([]int, 0, n) // longest increasing subseqence starting at index i

	for _, num := range nums {
		i := sort.Search(len(dp), func(j int) bool { return dp[j] >= num })

    if i == len(dp) {
      dp = append(dp, num)
    } else {
      dp[i] = num
    }

    maxLis = max(maxLis, len(dp))
	}

	return maxLis
}