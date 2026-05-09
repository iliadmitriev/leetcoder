func findTheDifference(s string, t string) byte {
    var res byte;
    for i := range s {
        res ^= s[i]
    }
    for i := range t {
        res ^= t[i]
    }
    return res
}