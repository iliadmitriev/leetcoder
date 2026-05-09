func minOperations(s string) int {
    one, zero := 0, 0
    f1, f2 := 0, 1

    for _, ch := range s {
        d := int(ch - '0')

        if f1 != d {
            one++
        }

        if f2 != d {
            zero++
        }

        f1, f2 = 1 - f1, 1 - f2
    }

    return min(one, zero)
}


func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}