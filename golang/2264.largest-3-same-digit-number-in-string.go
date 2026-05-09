func largestGoodInteger(num string) string {
    var cur byte = 47

    for i := 0; i < len(num) - 2; i++ {
        if num[i] == num[i + 1] && num[i] == num[i + 2] {
            if num[i] >= cur {
                cur = num[i]
            }
        }
    }

    if cur == 47 {
        return ""
    }

    return fmt.Sprintf("%c%c%c", cur, cur, cur)
}