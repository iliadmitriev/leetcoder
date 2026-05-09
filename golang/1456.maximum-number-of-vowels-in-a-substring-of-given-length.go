func maxVowels(s string, k int) int {
    maxVow := 0
    n := len(s)
    
    // build window
    curVow := 0
    for i := 0; i < k; i++ {
        curVow += isVowel(s[i])
    }
    maxVow = max(maxVow, curVow)

    // move window of size k
    for i := k; i < n; i++ {
        curVow -= isVowel(s[i - k])
        curVow += isVowel(s[i])
        maxVow = max(maxVow, curVow)
    }

    return maxVow
}

func isVowel(a byte) int {
    if a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' {
        return 1
    }
    return 0
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}