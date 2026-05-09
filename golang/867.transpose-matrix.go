func transpose(matrix [][]int) [][]int {
    m, n := len(matrix), len(matrix[0])

    if m == n {
        for i := 0; i < m; i++ {
            for j := i; j < n; j++ {
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            }
        }
        return matrix
    }

    res := make([][]int, n)

    for j := 0; j < n; j++ {
        res[j] = make([]int, m)
        for i := 0; i < m; i++ {
            res[j][i] = matrix[i][j]
        }
    }
    return res
}