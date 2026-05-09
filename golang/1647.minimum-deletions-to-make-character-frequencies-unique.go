func minDeletions(s string) int {
    n := 26

    frq := make([]int, n)
    for _, ch := range(s) {
        frq[ch - 'a']++
    }

    sort.Sort(sort.Reverse(sort.IntSlice(frq)))

    deletions := 0
    for i := 0; i < n - 1 && frq[i + 1] != 0; i++ {
        if frq[i] == 0 && frq[i + 1] >= 0 {
            deletions += frq[i + 1]
            frq[i + 1] = 0
        } else if frq[i] <= frq[i + 1] {
            diff := 1 + frq[i + 1] - frq[i]
            deletions += diff
            frq[i + 1] -= diff
        }
    }

    return deletions
}