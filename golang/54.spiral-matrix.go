func spiralOrder(matrix [][]int) []int {
    top, left := 0, 0
    bottom, right := len(matrix) - 1, len(matrix[0]) - 1
    res := make([]int, 0, len(matrix) * len(matrix[0]))

    for top <= bottom && left <= right {
        // top
        for c := left; c <= right; c++ {
            res = append(res, matrix[top][c])
        }
        top++
        // right
        for r := top; r <= bottom; r++ {
            res = append(res, matrix[r][right])
        }
        right--
        // bottom
        if top <= bottom {
            for c := right; c >= left; c-- {
                res = append(res, matrix[bottom][c])
            }
            bottom--
        }
        // left
        if left <= right {
            for r := bottom; r >= top; r-- {
                res = append(res, matrix[r][left])
            }
            left++
        }
    }
    
    return res
}