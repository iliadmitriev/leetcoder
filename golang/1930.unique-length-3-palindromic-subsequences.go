func countUnique(s []rune, i, j int) int {
    d := make(map[rune]bool, 26)
    for ; i < j; i++ {
        d[s[i]] = true
        if len(d) == 26 {
            return 26
        }
    }
    return len(d)
}

func countPalindromicSubsequence(s string) int {
    t := []rune(s)
    m := make(map[rune][]int, 26)

    for i := 0; i < len(t); i++ {
        m[t[i]] = append(m[t[i]], i)
    }

    res := 0
    for _, v := range m {
        if len(v) < 2 {
            continue
        }

        left := v[0] + 1
        right := v[len(v) - 1]

        res += countUnique(t, left, right)
    }
    return res
}