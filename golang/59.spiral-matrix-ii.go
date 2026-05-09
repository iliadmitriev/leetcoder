func generateMatrix(n int) [][]int {
    gen := 0;
    res := make([][]int, n)
    for i := 0; i < n; i++ { res[i] = make([]int, n) }
    loops := n / 2
    
    for l := 0; l < loops; l++ {
        // top row
        for c := l; c < n - l - 1; c++ {
            gen++
            res[l][c] = gen
        }
        // right column
        for r := l; r < n - l - 1; r++ {
            gen++
            res[r][n - l - 1] = gen
        }
        // bottom row
        for c := n - l - 1; c > l; c-- {
            gen++
            res[n - l - 1][c] = gen
        }
        // left column
        for r := n - l - 1; r > l; r-- {
            gen++
            res[r][l] = gen
        } 
    }

    if n % 2 == 1 {
        gen++
        res[n / 2][n / 2] = gen
    }

    return res;
}