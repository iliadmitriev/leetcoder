func minSteps(s string, t string) int {
    cache := make([]int, 26)

    for _, ch := range s {
        cache[ch - 'a']++
    }

    for _, ch := range t {
        cache[ch - 'a']--
    }

    res := 0

    for _, ch := range cache {
        if ch > 0 {
            res += ch
        }
    }

    return res
}