func makeEqual(words []string) bool {
    counts := make([]int, 26)
    for _, word := range words {
        for _, ch := range word {
            counts[ch - 'a']++
        }
    }
    n := len(words)
    for _, ch := range counts {
        if ch % n != 0 {
            return false
        }
    }
    return true
}