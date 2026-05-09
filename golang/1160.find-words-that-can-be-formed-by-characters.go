func countCharacters(words []string, chars string) int {
    var p [26]int
    for _, ch := range chars { p[ch - 'a']++ }
    res := 0
    add := 0

    for _, word := range words {
        add = len(word)
        if add > len(chars) {
            continue
        }

        var w [26]int
        for _, ch := range word { w[ch - 'a']++ }

        for i := 0; i < 26; i++ {
            if w[i] > p[i] {
                add = 0
                break
            }
        }
        res += add
    }

    return res
}