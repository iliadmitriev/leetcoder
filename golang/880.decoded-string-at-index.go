func decodeAtIndex(s string, k int) string {
    st := []rune(s)
    length := 0

    for i := 0; i < len(st); i++ {
        if unicode.IsDigit(st[i]) {
            length *= int(st[i] - '0')
        } else {
            length++
        }
    }
    fmt.Println(length)

    for i := len(st) - 1; i >= 0; i-- {
        k %= length

        if k == 0 && unicode.IsLetter(st[i]) {
            return string(st[i])
        } else if unicode.IsDigit(st[i]) {
            length /= int(st[i] - '0')
        } else {
            length--
        }
    }

    return ""
}