func arraySign(nums []int) int {
    total := 1
    for _, num := range nums {
        if num < 0 {
            total = -total
        } else if num == 0 {
            return 0
        }
    }

    return total
}