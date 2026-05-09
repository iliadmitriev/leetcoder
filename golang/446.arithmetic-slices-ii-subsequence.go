func numberOfArithmeticSlices(nums []int) int {
    res := 0
    n := len(nums)
    dp := make([]map[int]int, n)
    for i := range dp { dp[i] = make(map[int]int, i + 1) }

    var diff int
    for i := 0; i < n; i++ {
        for j := 0; j < i; j++ {
            diff = nums[i] - nums[j]
            dp[i][diff] += dp[j][diff] + 1
            res += dp[j][diff]
        }
    }

    return res
}