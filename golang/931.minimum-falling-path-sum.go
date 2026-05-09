func minFallingPathSum(matrix [][]int) int {
    m, n := len(matrix), len(matrix[0])

    cache := [2][]int{
        make([]int, n), make([]int, n),
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            min := cache[(i + 1) % 2][j]

            if j > 0 && min > cache[(i + 1) % 2][j - 1] {
                min = cache[(i + 1) % 2][j - 1]
            }

            if j < n - 1 && min > cache[(i + 1) % 2][j + 1] {
                min = cache[(i + 1) % 2][j + 1]
            }

            cache[i % 2][j] = matrix[i][j] + min
        }
    }

    res := cache[(m - 1) % 2][0]
    for _, v := range cache[(m - 1) % 2] {
        res = min(res, v)
    }

    return res
}
