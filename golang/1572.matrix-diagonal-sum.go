func diagonalSum(mat [][]int) int {
    total := 0
    n := len(mat)

    for i := 0; i < n; i++ {
        total += mat[i][i] + mat[i][n - i - 1]
    }

    if n % 2 == 1 {
        total -= mat[n / 2][n / 2]
    }

    return total
}