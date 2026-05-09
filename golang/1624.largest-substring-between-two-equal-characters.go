func maxLengthBetweenEqualCharacters(s string) int {
    cache := [26]int{}
    for i := 0; i < 26; i++ {cache[i] = -1}
    
    res := -1
    for r, ch := range s {
        
        if l := cache[int(ch - 'a')]; l != -1 {
            res = max(res, r - l - 1)
        } else {
            cache[int(ch - 'a')] = r
        }
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}