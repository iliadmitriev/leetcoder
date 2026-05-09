func isSubsequence(s string, t string) bool {
    n := len(t)
    m := len(s)

    j := 0

    for i := 0; i < n && j < m; i++ {
        if t[i] == s[j] {
            j++
        }
    }

    return m == j
}