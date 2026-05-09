func numIdenticalPairs(nums []int) int {
    cache := make(map[int]int)
    out := 0
    for _, num := range nums {
        if value, ok := cache[num]; ok {
            out += value
        }
        cache[num]++
    }
    return out
}