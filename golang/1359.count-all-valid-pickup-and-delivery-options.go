const mod = 1e9 + 7

func countOrders(n int) int {
    res := 1
    valid_choises := 1
    
    for i := 1; i <= n; i++ {
        valid_choises = i * (2 * i - 1)
        res *= valid_choises
        res %= mod
    }

    return res
}