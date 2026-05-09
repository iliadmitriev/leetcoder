const N = 26

func closeStrings(word1 string, word2 string) bool {
    n1, n2 := len(word1), len(word2)

    if n1 != n2 {
        return false
    }

    w1, w2 := [N]int{}, [N]int{}
    ex1, ex2 := [N]bool{}, [N]bool{}

    for i := 0; i < n1; i++ {
        w1[word1[i] - 'a']++
        w2[word2[i] - 'a']++
        ex1[word1[i] - 'a'] = true
        ex2[word2[i] - 'a'] = true
    }

    sort.Ints(w1[:])
    sort.Ints(w2[:])

    return w1 == w2 && ex1 == ex2
}