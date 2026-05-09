func reorganizeString(s string) string {
    charCounts := make(map[rune]int)
    for _, ch := range s {
        charCounts[ch]++
    }
    maxCount := 0
    var maxLetter rune
    for ch := range charCounts {
        if charCounts[ch] > maxCount {
            maxCount = charCounts[ch]
            maxLetter = ch
        }
    }

    if maxCount > (len(s) + 1) / 2 {
        return ""
    }

    res := make([]rune, len(s))
    index := 0

    for charCounts[maxLetter] > 0 {
        res[index] = maxLetter
        index += 2
        charCounts[maxLetter]--
    }

    for ch := range charCounts {
        for charCounts[ch] > 0 {
            if index >= len(s) {
                index = 1
            }
            res[index] = ch
            index += 2
            charCounts[ch]--
        }
    }

    return string(res)
}