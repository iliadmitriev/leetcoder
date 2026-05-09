func minCostClimbingStairs(cost []int) int {
        // cost to get to k-2 index and k-1
        // (two previous values before k)
        var k_2, k_1, k int

        for i := 2; i <= len(cost); i++ {
            k = min(k_1 + cost[i - 1], k_2 + cost[i - 2])
            k_2 = k_1
            k_1 = k
        }
        return k
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}