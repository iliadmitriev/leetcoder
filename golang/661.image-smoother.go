func avg3x3(arr [][]int, y, x int) int {
    m, n := len(arr), len(arr[0])
    res, cnt := 0, 0

    for i := max(0, y - 1); i < min(m, y + 2); i++ {
        for j := max(0, x - 1); j < min(n, x + 2); j++ {
            res += arr[i][j]
            cnt++
        }
    }

    return res / cnt
}

func imageSmoother(img [][]int) [][]int {
    m, n := len(img), len(img[0])
    res := make([][]int, m)

    for i := 0; i < m; i++ {
        res[i] = make([]int, n)
        for j := 0; j < n; j++ {
            res[i][j] = avg3x3(img, i, j)
        }
    }

    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}