func findLeastNumOfUniqueInts(arr []int, k int) int {
    freq := make(map[int]int)
    for _, num := range arr { freq[num]++ }

    res := len(freq)
    n := len(arr)
    quef := make([]int, n + 1)

    for _, f := range freq {
        quef[f]++
    }

    for f := 1; f <= n; f++ {
        if k >= quef[f] * f {
            k -= quef[f] * f
            res -= quef[f]
        } else {
            res -= k / f
            break
        }
    }

    return res
}