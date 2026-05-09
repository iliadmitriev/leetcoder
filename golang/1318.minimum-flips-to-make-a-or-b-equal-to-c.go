func popcount(a int) int {
    count := 0
    for a > 0 {
        a &= a - 1
        count++
    }
    return count
}

func minFlips(a int, b int, c int) int {
    return popcount((a | b) ^ c) + popcount(a & b & ^c)
}