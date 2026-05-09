func kthGrammar(n int, k int) int {
    cur := 0
    left := 0
    right := 1 << (n - 1)
    var mid int
    for  i := 0; i < n - 1; i++ {
        mid = (left + right) / 2
        if k > mid {
            left = mid + 1
            cur = 1 - cur
        } else {
            right = mid
        }
    }

    return cur
}