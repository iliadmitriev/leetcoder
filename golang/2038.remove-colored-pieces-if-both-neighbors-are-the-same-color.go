func winnerOfGame(colors string) bool {
    a, b := 0, 0
    l, r := 0, 0

    for l < len(colors) {
        for r < len(colors) && colors[l] == colors[r] {
            r++
        }

        if colors[l] == 'A' {
            a += max(0, r - l - 2)
        } else {
            b += max(0, r - l - 2)
        }
        l = r
    }

    return a > b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}