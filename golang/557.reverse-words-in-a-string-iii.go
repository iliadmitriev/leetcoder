import (
    "strings"
)


func reverseWords(s string) string {
    words := strings.Split(s, " ")
    for i, word := range words {
        words[i] = revWord(word)
    }
    return strings.Join(words, " ")
}

func revWord(s string) string {
    n := len(s)
    r := []rune(s)
    for i := 0; i < n / 2; i++ {
        r[i], r[n - i - 1] = r[n - i - 1], r[i]
    }
    return string(r)
}