func pal(s *string, l, r int) int {
    t := *s
    count := 0

    for l >= 0 && r < len(t) && t[l] == t[r] {
        count++
        l--
        r++
    }

    return count
}

func countSubstrings(s string) int {
    count := 0

    for i := 0; i < len(s); i++ {
        count += pal(&s, i, i) + pal(&s, i, i + 1)
    }

    return count
}