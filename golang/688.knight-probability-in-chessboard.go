func knightProbability(n int, k int, row int, column int) float64 {

    cache := make(map[Key]float64)
    
    return dfs(row, column, 0, cache, k, n)
}

type Key struct{
    i, j, move int
}

var dirs = [][]int{
        []int{1, 2}, []int{1, -2}, []int{-1, 2}, []int{-1, -2},
        []int{2, 1}, []int{2, -1}, []int{-2, 1}, []int{-2, -1},
    }

func dfs(i, j, move int, cache map[Key]float64, k, n int) float64 {
    // if we already have needed value calculated
    // then return it and don't calculate it again
    key := Key{i, j, move}
    if val, ok := cache[key]; ok {
        return val
    }

    // if we have went off the chessboard
    if i < 0 || i >= n || j < 0 || j >= n {
        return 0.0 // return 0 probability
    }

    if move == k {
        return 1.0
    }

    // symmetry optimization
    mid := (n / 2) + (n % 2)
    if i > j || i >= mid || j >= mid {
        if i > j { i, j = j, i }
        i, j = min(i, n - 1 - i), min(j, n - 1 - j)

        return dfs(i, j, move, cache, k, n)
    }

    // calculate result resursively
    result := 0.0
    for _, step := range dirs {
        // make a step
        result += dfs(i + step[0], j + step[1], move + 1, cache, k, n)
    }
    // it's eight possible moves
    result /= 8

    // save result to cache and return it
    cache[key] = result
    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}