const MOD = int(1e9) + 7

func countVowelPermutation(n int) int {
    a, e, i, o, u := 1, 1, 1, 1, 1

    for ; n > 1; n-- {
        a, e, i, o, u = 
            (e + i + u) % MOD,
            (a + i) % MOD,
            (e + o) % MOD,
            (i) % MOD,
            (i + o) % MOD
    }

    return (a + e + i + o + u) % MOD
}