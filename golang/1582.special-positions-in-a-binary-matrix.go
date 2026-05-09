func numSpecial(mat [][]int) int {
    m, n := len(mat), len(mat[0])
    special := 0

    rows := make([]int, m)
    cols := make([]int, n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 1 {
                rows[i]++
                cols[j]++
            }
        }
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1 {
                special++
            }
        }
    }

    return special
}