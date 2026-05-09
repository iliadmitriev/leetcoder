func findContentChildren(g []int, s []int) int {

    sort.Ints(s)
    sort.Ints(g)

    n, m := len(g), len(s)

    i, j := 0, 0

    for i < n && j < m {
        if g[i] <= s[j] {
            i++
        }
        j++
    }

    return i
}