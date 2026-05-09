func longestStrChain(words []string) int {
    cache := make(map[string]int)
    res := 0

    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) < len(words[j])
    })

    for _, word := range words {
        maxValue := 0
        for j := 0; j < len(word); j++ {
            key := word[0:j] + word[j + 1: len(word)]
            if cache[key] > maxValue { maxValue = cache[key] }
        }
        cache[word] = 1 + maxValue
        if cache[word] > res { res = cache[word] }
    }

    return res
}