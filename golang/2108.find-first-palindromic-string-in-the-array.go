func pal(word *string) bool {
    w := *word
    i, j := 0, len(w) - 1

    for i < j {
        if w[i] != w[j] {
            return false
        }

        i++
        j--
    }

    return true
}

func firstPalindrome(words []string) string {
    for i := range words {
        if pal(&words[i]) {
            return words[i]
        }
    }

    return ""
}