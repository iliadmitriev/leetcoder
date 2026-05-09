func uniqueOccurrences(arr []int) bool {
    counter := make(map[int]int)
    cache := make(map[int]int)

    for _, num := range arr {
        counter[num]++;
    }

    for _, v := range counter {
        if _, ok := cache[v]; ok {
            return false
        }
        cache[v] = 1
    }

    return true
}