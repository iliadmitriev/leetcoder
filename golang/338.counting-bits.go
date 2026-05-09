func countBits(n int) []int {
    l := n + 1
    res := make([]int, l)
    
    for i := 1; i < l; i++ {
        res[i] = res[i & (i - 1)] + 1
    }

    return res
}