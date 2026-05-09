func rangeBitwiseAnd(left int, right int) int {
    count := 0
    
    for left != right {
        left >>= 1
        right >>= 1
        count++
    }

    return right << count
}