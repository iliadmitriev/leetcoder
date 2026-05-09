func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    flag := true
    i1, i2 := 0, 0
    c1, c2 := 0, 0
    n1, n2 := len(word1), len(word2)

    for i1 < n1 && i2 < n2 {
        if word1[i1][c1] != word2[i2][c2] {
            flag = false
            break
        }

        c1++
        c2++

        if c1 == len(word1[i1]) {
            c1 = 0
            i1++
        }
        if c2 == len(word2[i2]) {
            c2 = 0
            i2++
        }
    }

    if flag {
        flag = i1 == n1 && i2 == n2
    }

    return flag
}