func convertToTitle(columnNumber int) string {
    res := ""
    for columnNumber > 0 {
        columnNumber--
        charCode := 'A' + rune(columnNumber % 26)
        res = string(charCode) + res
        columnNumber /= 26
    }
    return res
}