func lengthOfLongestSubstring(s string) int {
    n := len(s)
    maxNonRep := 0
    cache := make([]bool, 256)

    for i, j := 0, 0; i < n; i++ {
        for cache[s[i]] {
            cache[s[j]] = false
            j++
        }

        cache[s[i]] = true

        if i - j + 1 > 0 {
            maxNonRep = max(maxNonRep, i - j + 1)
        }
    }

    return maxNonRep
}