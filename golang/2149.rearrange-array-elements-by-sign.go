func rearrangeArray(nums []int) []int {
    n := len(nums)
    cache := make([]int, n)

    i, j := 0, 1

    for k := 0; k < n; k++ {
        if nums[k] < 0 {
            cache[j] = nums[k]
            j += 2
        } else {
            cache[i] = nums[k]
            i += 2
        }
    }

    return cache
}