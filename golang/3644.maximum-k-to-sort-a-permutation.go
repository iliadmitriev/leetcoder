func sortPermutation(nums []int) int {
    res := -1

    for i, num := range nums {
        if num == i {
            continue
        }

        res &= num
    }

    if res == -1 {
        return 0
    }

    return res
}