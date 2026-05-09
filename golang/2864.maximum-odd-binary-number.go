func maximumOddBinaryNumber(s string) string {
    n := len(s)
    res := make([]byte, n)
    cnt1 := 0

    for _, c := range s {
        if c == '1' {
            cnt1++
        }
    }

    cnt1--
    n--

    for i := 0; i < cnt1; i++ {
        res[i] = '1'
    }

    for i := cnt1; i < n; i++ {
        res[i] = '0'
    }

    res[n] = '1'

    return string(res)
}