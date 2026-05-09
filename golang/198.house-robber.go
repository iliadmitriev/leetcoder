func rob(nums []int) int {
    dp, dp_prev := 0, 0

    for _, num := range nums {
        dp, dp_prev = max(dp_prev + num, dp), dp
    }

    return dp
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}