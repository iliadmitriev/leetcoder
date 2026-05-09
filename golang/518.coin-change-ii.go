func change(amount int, coins []int) int {
    dp := make([]int, amount + 1)
    dp[0] = 1

    for _, coin := range coins {
        for value := coin; value <= amount; value++ {
            dp[value] += dp[value - coin]
        }
    }

    return dp[amount]
    
}