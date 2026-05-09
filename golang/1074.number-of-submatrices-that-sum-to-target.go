func numSubmatrixSumTarget(matrix [][]int, target int) int {
    m, n := len(matrix), len(matrix[0])

    prefix := make([][]int, m + 1)
    prefix[0] = make([]int, n + 1)
    for i := 1; i <= m; i++ {
        prefix[i] = make([]int, n + 1)
        for j := 1; j <= n; j++ {
            prefix[i][j] = matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        }
    }

    count := 0

    for r1 := 1; r1 <= m; r1++ {
        for r2 := r1; r2 <= m; r2++ {

            // refs to leetcode 560
            cache := make(map[int]int, n)
            cache[0] = 1

            for c := 1; c <= n; c++ {
                total := prefix[r2][c] - prefix[r1 - 1][c]
                count += cache[total - target]
                cache[total]++
            }
        }
    }

    return count
}