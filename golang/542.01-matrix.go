func updateMatrix(mat [][]int) [][]int {
    if len(mat) == 0 || len(mat[0]) == 0 {
        return mat
    }

    m, n := len(mat), len(mat[0])
    MAX := m * n // +inf

    queue := make([]int, 0, MAX * 2)

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 0 {
                queue = append(queue, i, j)
            } else {
                mat[i][j] = MAX
            }
        }
    }

    phase := []int{-1, 0, 1, 0, -1}

    for len(queue) > 0 {
        row, col := queue[0], queue[1]
        queue = queue[2:]

        for i := 0; i < 4; i++ {
            r, c := row + phase[i], col + phase[i + 1]
            if r >= 0 && r < m && c >=0 && c < n && mat[r][c] > mat[row][col] + 1 {
                queue = append(queue, r, c)
                mat[r][c] = mat[row][col] + 1
            }
        }
    }

    return mat
    
}