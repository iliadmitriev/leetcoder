func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    res := [26]int{}
    base := 'a'
    for _, r := range s {
        res[r - base]++
    }

    for _, r := range t {
        if res[r - base] == 0 {
            return false
        }
        
        res[r - base]--
    }

    return true
}