func minOperations(nums []int) int {
    cache := make(map[int]int)
    for _, num := range nums {
        cache[num]++
    }

    res := 0
    for _, v := range cache {
        if v == 1 {
            return -1
        }
        res += v / 3
        if v % 3 > 0 {
            res++
        }
    }

    return res
}