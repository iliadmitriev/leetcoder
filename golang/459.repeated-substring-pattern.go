func repeatedSubstringPattern(s string) bool {
    n := len(s)
    for size := 1; size <= n / 2; size++ {
        if n % size == 0 && strings.Repeat(s[0: size], n / size) == s {
            return true
        }
    }
    return false
}